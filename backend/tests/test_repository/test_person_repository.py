import re
from datetime import datetime
from random import choice

import pytest
from faker import Faker

from src.database import DatabaseConfig
from src.database.tables.base_table import timezoneUTC
from src.person.person_repository import PersonRepository
from src.person.schema.person_fields import EnumGender
from src.person.schema.person_filter import PersonFilterFULL
from src.person.schema.person_schema import PersonSchemaFULL
from src.person.schema.person_schema import PersonSchemaPOST


repository = PersonRepository(DatabaseConfig.test_config.sessionmaker)

uuid4_hex_regex = re.compile(
    "^[0-9A-F]{12}4[0-9A-F]{3}[89AB][0-9A-F]{15}$",
    flags=re.I,
)

fake = Faker(['ru_RU'])


def person_data_factory() -> PersonSchemaPOST:
    gender = choice(['male', 'female'])
    if gender == 'male':
        *_, name, patronymic, surname = fake.name_male().split()
    elif gender == 'female':
        *_, name, patronymic, surname = fake.name_female().split()
    birth_date = fake.date_of_birth(minimum_age=0, maximum_age=90)

    return PersonSchemaPOST(
        name=name,
        surname=surname,
        patronymic=patronymic,
        gender=getattr(EnumGender, gender),
        birth_date=birth_date,
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
