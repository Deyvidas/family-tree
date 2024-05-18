from random import choice

from faker import Faker

from src.person.repository.person_repository_dto import PersonSchemaInsert
from src.person.schema.person_fields import EnumGender


fake = Faker(['ru_RU'])


def generate_person() -> PersonSchemaInsert:
    gender = choice(list(EnumGender))
    birth_date = fake.date_of_birth(minimum_age=0, maximum_age=90)

    match gender.value:
        case 'male':
            *_, name, patronymic, surname = fake.name_male().split()
        case 'female':
            *_, name, patronymic, surname = fake.name_female().split()

    return PersonSchemaInsert(
        name=name,
        surname=surname,
        patronymic=patronymic,
        gender=getattr(EnumGender, gender),
        birth_date=birth_date,
    )
