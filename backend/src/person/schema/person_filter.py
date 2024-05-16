from pydantic import Field

from src.common.schema.filter import BaseFilter
from src.common.schema.filter import BaseModelForFilter

from .person_fields import PersonSchemaFields


class PersonFilter(BaseModelForFilter):
    name: PersonSchemaFields.name = Field(default=None)
    surname: PersonSchemaFields.surname = Field(default=None)
    patronymic: PersonSchemaFields.patronymic = Field(default=None)
    gender: PersonSchemaFields.gender = Field(default=None)
    birth_date: PersonSchemaFields.birth_date = Field(default=None)


class PersonFilterFULL(BaseFilter, PersonFilter):
    pass
