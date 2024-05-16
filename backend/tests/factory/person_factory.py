from random import choice

from faker import Faker

from src.person.schema.person_fields import EnumGender
from src.person.schema.person_schema import PersonSchemaPOST


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
