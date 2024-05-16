from datetime import date
from enum import Enum
from typing import Annotated

from pydantic import Field


class EnumGender(Enum):
    male = 'male'
    female = 'female'


class PersonSchemaFields:
    name = Annotated[
        str,
        Field(),
    ]
    surname = Annotated[
        str,
        Field(),
    ]
    patronymic = Annotated[
        str,
        Field(),
    ]
    gender = Annotated[
        EnumGender,
        Field(),
    ]
    birth_date = Annotated[
        date,
        Field(),
    ]