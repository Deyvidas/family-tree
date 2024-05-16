import re
from datetime import datetime
from random import choice
from typing import Any

import pytest
from sqlalchemy import select

from src.database.tables.base_table import timezoneUTC
from src.person.person_repository import PersonRepository
from src.person.schema.person_filter import PersonFilterFULL
from src.person.schema.person_schema import PersonSchemaFULL
from src.person.schema.person_schema import PersonSchemaPOST
from tests.factory.person_factory import generate_person


repository = PersonRepository.sql_alchemy_test


def validate_person(valid_data: Any, to_validate_data: Any) -> None:
    uuid4_hex_regex = re.compile("^[0-9A-F]{12}4[0-9A-F]{3}[89AB][0-9A-F]{15}$", flags=re.I)  # fmt:skip # noqa:E501
    valid = PersonSchemaPOST.model_validate(valid_data)
    to_validate = PersonSchemaFULL.model_validate(to_validate_data)

    for attr in valid.model_fields.keys():
        assert getattr(valid, attr) == getattr(to_validate, attr)

    assert re.fullmatch(uuid4_hex_regex, to_validate.id)
    assert to_validate.created_at == datetime.now(timezoneUTC)
    assert to_validate.updated_at == datetime.now(timezoneUTC)


@pytest.fixture
def populate_database() -> list[PersonSchemaFULL]:
    GENERATE_QUANTITY = 20
    people_to_insert = [generate_person() for _ in range(GENERATE_QUANTITY)]
    people_list = repository.bulk_create(people_to_insert)
    assert len(people_list) == GENERATE_QUANTITY
    return people_list


@pytest.mark.usefixtures('use_database')
class TestCreate:
    def test_base(self, freezer):
        """
        Test whether we can insert one row into the database and that it will
        be returned with additional generic fields, such as id, created_at, etc
        """
        person_data = generate_person()
        person = repository.create(person_data)
        assert isinstance(person, PersonSchemaFULL)

        # Check if the person is really created in the database.
        stmt = select(repository.table).filter_by(id=person.id)
        with repository.sessionmaker() as session:
            # Return exactly one object or raise an exception.
            person = session.scalars(stmt).one()
        validate_person(person_data, person)


@pytest.mark.usefixtures('use_database')
class TestBulkCreate:
    def test_base(self, freezer):
        """
        Test whether we can insert many rows into the database and that all of
        them will be returned with additional generic fields, such as id,
        created_at, etc
        """
        people_data = [generate_person() for _ in range(5)]
        inserted = repository.bulk_create(people_data)
        assert len(inserted) == 5
        assert all(map(lambda p: isinstance(p, PersonSchemaFULL), inserted))

        # Check if they are really created in the database
        for data in people_data:
            stmt = select(repository.table).filter_by(**data.model_dump())
            with repository.sessionmaker() as session:
                # Return exactly one object or raise an exception.
                created_person = session.scalars(stmt).one()
            validate_person(data, created_person)


@pytest.mark.usefixtures('use_database')
class TestFilter:
    def test_base(self, populate_database: list[PersonSchemaFULL]):
        """
        Test whether we can filter database rows using correct filters
        """
        person_to_get = choice(populate_database)
        can_filter_by = PersonFilterFULL.model_fields.keys()

        # Filtering using one filter parameter
        for attr in can_filter_by:
            filter = PersonFilterFULL(**{attr: getattr(person_to_get, attr)})
            found = repository.filter(filter)
            assert len(found) >= 1

        # Filtering using all available filter parameters
        filter_kwargs = {a: getattr(person_to_get, a) for a in can_filter_by}
        filter = PersonFilterFULL(**filter_kwargs)
        found = repository.filter(filter)
        assert len(found) == 1
        assert isinstance(found[0], PersonSchemaFULL)

    def test_without_filter_by(
        self,
        populate_database: list[PersonSchemaFULL],
    ):
        """
        Test that all rows from the database are returned by the method
        .filter() without filters
        """
        received_people = repository.filter()
        assert len(received_people) == len(populate_database)

    def test_with_order_by(
        self,
        populate_database: list[PersonSchemaFULL],
    ):
        """Test that ordering work correct"""
        ordered_people = repository.filter(order_by=['gender', '-birth_date'])
        assert len(ordered_people) == len(populate_database)

        for i in range(len(ordered_people) - 2):
            left, right = ordered_people[i], ordered_people[i + 1]

            assert left.gender <= right.gender
            if left.gender == right.gender:
                assert left.birth_date >= right.birth_date
