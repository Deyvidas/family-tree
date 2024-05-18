from datetime import date
from enum import Enum
from typing import Annotated

from pydantic import Field

from src.common.schema.fields import BaseFields


class EnumGender(str, Enum):
    male = 'male'
    female = 'female'


class PersonFields(BaseFields):
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
