import re
from datetime import datetime
from random import choice

import pytest
from sqlalchemy import select

from src.database import DatabaseConfig
from src.database.tables.base_table import timezoneUTC
from src.person.person_repository import PersonRepository
from src.person.schema.person_filter import PersonFilterFULL
from src.person.schema.person_schema import PersonSchemaFULL
from tests.factory.person_factory import person_data_factory


repository = PersonRepository(DatabaseConfig.test_config.sessionmaker)

uuid4_hex_regex = re.compile(
    "^[0-9A-F]{12}4[0-9A-F]{3}[89AB][0-9A-F]{15}$",
    flags=re.I,
)


@pytest.fixture
def populate_database() -> list[PersonSchemaFULL]:
    people_to_insert = [person_data_factory() for _ in range(20)]
    return [
        repository.create(**person.model_dump()) for person in people_to_insert
    ]


@pytest.mark.usefixtures('use_database')
class Test:
    def test_create(self, freezer):
        """
        Test that we can create one instance and after creation, it will be
        returned with additional generic fields, e.g. id, created_at, etc.
        """
        person_data = person_data_factory()
        person = repository.create(**person_data.model_dump())
        assert isinstance(person, PersonSchemaFULL)

        # Check if the person is really created in the database.
        stmt = select(repository.table).filter_by(id=person.id)
        with repository.sessionmaker() as session:
            session.scalars(stmt).one()

        assert person.name == person_data.name
        assert person.surname == person_data.surname
        assert person.patronymic == person_data.patronymic
        assert person.gender == person_data.gender
        assert person.birth_date == person_data.birth_date

        assert re.fullmatch(uuid4_hex_regex, person.id)
        assert person.created_at == datetime.now(timezoneUTC)
        assert person.updated_at == datetime.now(timezoneUTC)

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
