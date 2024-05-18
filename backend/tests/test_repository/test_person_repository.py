import re
from datetime import datetime
from random import choice
from typing import Any

import pytest
from sqlalchemy import select

from src.database.tables.base_table import timezoneUTC
from src.person.repository.person_repository import PersonRepositories
from src.person.repository.person_repository_dto import PersonSchemaInsert
from src.person.schema.person_schema import PersonSchema
from tests.factory.person_factory import generate_person


repository = PersonRepositories.sqlalchemy_test


def validate_person(valid_data: Any, to_validate_data: Any) -> None:
    uuid4_hex_regex = re.compile("^[0-9A-F]{12}4[0-9A-F]{3}[89AB][0-9A-F]{15}$", flags=re.I)  # fmt:skip # noqa:E501
    valid = PersonSchemaInsert.model_validate(valid_data)
    to_validate = PersonSchema.model_validate(to_validate_data)

    for attr in valid.model_fields_set:
        assert getattr(valid, attr) == getattr(to_validate, attr)

    assert re.fullmatch(uuid4_hex_regex, to_validate.id)
    assert to_validate.created_at == datetime.now(timezoneUTC)
    assert to_validate.updated_at == datetime.now(timezoneUTC)


@pytest.fixture
def populate_database() -> list[PersonSchema]:
    GENERATE_QUANTITY = 20
    people_to_insert = [generate_person() for _ in range(GENERATE_QUANTITY)]
    new_people_list = repository.bulk_create(people_to_insert)
    assert len(new_people_list) == GENERATE_QUANTITY
    return new_people_list


@pytest.mark.usefixtures('use_database')
class TestCreate:
    @pytest.mark.usefixtures('freezer')
    def test_base(self):
        """
        Test whether we can insert one row into the database and that it will
        be returned with additional generic fields, such as id, created_at, etc
        """
        new_person_data = generate_person()
        new_person = repository.create(new_person_data)
        assert isinstance(new_person, PersonSchema)

        # Check if the person is really created in the database.
        stmt = select(repository.table).filter_by(id=new_person.id)
        with repository.sessionmaker() as session:
            # Return exactly one object or raise an exception.
            new_person = session.scalars(stmt).one()
        validate_person(new_person_data, new_person)


@pytest.mark.usefixtures('use_database')
class TestBulkCreate:
    @pytest.mark.usefixtures('freezer')
    def test_base(self):
        """
        Test whether we can insert many rows into the database and that all of
        them will be returned with additional generic fields, such as id,
        created_at, etc
        """
        people_data_list = [generate_person() for _ in range(5)]
        new_people = repository.bulk_create(people_data_list)
        assert len(new_people) == 5
        assert all(map(lambda p: isinstance(p, PersonSchema), new_people))

        # Check if they are really created in the database
        for person_data in people_data_list:
            stmt = select(repository.table).filter_by(
                **person_data.model_dump()
            )
            with repository.sessionmaker() as session:
                new_person = session.scalars(stmt).one()
            validate_person(person_data, new_person)


@pytest.mark.usefixtures('use_database')
class TestFilter:
    def test_base(self, populate_database: list[PersonSchema]):
        """
        Test whether we can filter database rows using correct filters
        """
        person_to_get = choice(populate_database)
        can_filter_by = PersonSchema.model_fields.keys()

        # Filtering using one filter parameter
        for attr in can_filter_by:
            filter_by = {attr: getattr(person_to_get, attr)}
            found = repository.filter(filter_by=filter_by)
            assert len(found) >= 1

        # Filtering using all available filter parameters
        filter_by_all = {a: getattr(person_to_get, a) for a in can_filter_by}
        found = repository.filter(filter_by_all)
        assert len(found) == 1
        assert isinstance(found[0], PersonSchema)

    def test_without_filter_by(
        self,
        populate_database: list[PersonSchema],
    ):
        """
        Test that all rows from the database are returned by the method
        .filter() without filters
        """
        received_people = repository.filter()
        assert len(received_people) == len(populate_database)

    def test_with_order_by(
        self,
        populate_database: list[PersonSchema],
    ):
        """Test that ordering work correct"""
        ordered_people = repository.filter(order_by=['gender', '-birth_date'])
        assert len(ordered_people) == len(populate_database)

        for left, right in zip(ordered_people[:-1], ordered_people[1:]):
            assert left.gender <= right.gender
            if left.gender == right.gender:
                assert left.birth_date >= right.birth_date
