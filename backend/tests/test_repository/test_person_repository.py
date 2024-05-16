import re
from datetime import datetime
from random import choice
from typing import Any

import pytest
from sqlalchemy import select

from src.database import DatabaseConfig
from src.database.tables.base_table import timezoneUTC
from src.person.person_repository import PersonRepository
from src.person.schema.person_filter import PersonFilterFULL
from src.person.schema.person_schema import PersonSchemaFULL
from src.person.schema.person_schema import PersonSchemaPOST
from tests.factory.person_factory import generate_person


repository = PersonRepository(DatabaseConfig.test_config.sessionmaker)


@pytest.fixture
def populate_database() -> list[PersonSchemaFULL]:
    people_to_insert = [generate_person().model_dump() for _ in range(20)]
    return repository.bulk_create(people_to_insert)


@pytest.mark.usefixtures('use_database')
class Test:
    def test_create(self, freezer):
        """
        Test whether we can insert one row into the database and that it will
        be returned with additional generic fields, such as id, created_at, etc
        """
        person_data = generate_person()
        person = repository.create(**person_data.model_dump())
        assert isinstance(person, PersonSchemaFULL)

        # Check if the person is really created in the database.
        stmt = select(repository.table).filter_by(id=person.id)
        with repository.sessionmaker() as session:
            # Return exactly one object or raise an exception.
            person = session.scalars(stmt).one()
        self.validate_person(person_data, person)

    def test_bulk_create(self, freezer):
        """
        Test whether we can insert many rows into the database and that all of
        them will be returned with additional generic fields, such as id,
        created_at, etc
        """
        people_to_insert = [generate_person().model_dump() for _ in range(5)]
        inserted = repository.bulk_create(people_to_insert)
        assert len(inserted) == 5
        assert all(map(lambda p: isinstance(p, PersonSchemaFULL), inserted))

        # Check if they are really created in the database
        for person in people_to_insert:
            stmt = select(repository.table).filter_by(**person)
            with repository.sessionmaker() as session:
                # Return exactly one object or raise an exception.
                created_person = session.scalars(stmt).one()
            self.validate_person(person, created_person)

    def test_filter(self, populate_database: list[PersonSchemaFULL]):
        """
        Test whether we can filter database rows using correct filters.
        """
        person_to_get = choice(populate_database)
        can_filter_by = PersonFilterFULL.model_fields.keys()

        for attr in can_filter_by:
            filter = PersonFilterFULL(**{attr: getattr(person_to_get, attr)})
            found = repository.filter(**filter.model_dump(exclude_unset=True))
            assert len(found) >= 1

        filter_kwargs = {a: getattr(person_to_get, a) for a in can_filter_by}
        filter = PersonFilterFULL(**filter_kwargs)
        found = repository.filter(**filter.model_dump())
        assert len(found) == 1
        assert isinstance(found[0], PersonSchemaFULL)

    def validate_person(self, valid_data: Any, to_validate_data: Any) -> None:
        uuid4_hex_regex = re.compile("^[0-9A-F]{12}4[0-9A-F]{3}[89AB][0-9A-F]{15}$", flags=re.I)  # fmt:skip # noqa:E501
        valid = PersonSchemaPOST.model_validate(valid_data)
        to_validate = PersonSchemaFULL.model_validate(to_validate_data)

        for attr in valid.model_fields.keys():
            assert getattr(valid, attr) == getattr(to_validate, attr)

        assert re.fullmatch(uuid4_hex_regex, to_validate.id)
        assert to_validate.created_at == datetime.now(timezoneUTC)
        assert to_validate.updated_at == datetime.now(timezoneUTC)
