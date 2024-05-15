import re
from datetime import date
from datetime import datetime

import pytest

from src.database import DatabaseConfig
from src.database.tables.base_table import timezoneUTC
from src.person.person_repository import PersonRepository
from src.person.person_schema import EnumGender
from src.person.person_schema import PersonSchema
from src.person.person_schema import PersonSchemaPOST


repository = PersonRepository(DatabaseConfig.test_config.sessionmaker)

uuid4_hex_regex = re.compile(
    "^[0-9A-F]{12}4[0-9A-F]{3}[89AB][0-9A-F]{15}$",
    flags=re.I,
)


@pytest.fixture
def person_data():
    return PersonSchemaPOST(
        name='Name',
        surname='Surname',
        patronymic='Patronymic',
        gender=EnumGender.male,
        birth_date=date(year=1990, month=3, day=15),
    )


@pytest.mark.usefixtures('use_database')
class Test:
    def test_create(self, freezer, person_data: PersonSchemaPOST):
        """
        Test that we can create one instance and after creation, it will be
        returned with additional generic fields, e.g. id, created_at, etc.
        """
        person = repository.create(**person_data.model_dump())

        assert isinstance(person, PersonSchema)
        assert person.name == person_data.name
        assert person.surname == person_data.surname
        assert person.patronymic == person_data.patronymic
        assert person.gender == person_data.gender
        assert person.birth_date == person_data.birth_date

        assert re.fullmatch(uuid4_hex_regex, person.id)
        assert person.created_at == datetime.now(timezoneUTC)
        assert person.updated_at == datetime.now(timezoneUTC)
