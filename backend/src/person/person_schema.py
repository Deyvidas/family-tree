from datetime import date
from enum import Enum

from pydantic import BaseModel

from src.common.schema import BaseSchema


class EnumGender(Enum):
    male = 'male'
    female = 'female'


class PersonSchema(BaseSchema):
    name: str
    surname: str
    patronymic: str
    gender: EnumGender
    birth_date: date


class PersonSchemaPOST(BaseModel):
    name: str
    surname: str
    patronymic: str
    gender: EnumGender
    birth_date: date
