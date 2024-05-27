from datetime import date
from enum import Enum
from typing import Annotated

from pydantic import Field

from src.common.schema import BaseFields


class GenderEnum(str, Enum):
    female = 'female'
    male = 'male'


class Fields(BaseFields):
    name = Annotated[
        str,
        Field(),
    ]
    surname = Annotated[
        str,
        Field(),
    ]
    surname_at_birth = Annotated[
        str,
        Field(),
    ]
    patronymic = Annotated[
        str,
        Field(),
    ]
    gender = Annotated[
        GenderEnum,
        Field(),
    ]
    birth_date = Annotated[
        date,
        Field(),
    ]
    dead_date = Annotated[
        date,
        Field(),
    ]
