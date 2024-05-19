from src.common.schema.config import BaseModelForSchema
from src.common.schema.schema import BaseSchema

from .person_fields import PersonFields


class PersonSchema(BaseSchema):
    name: PersonFields.name
    surname: PersonFields.surname
    patronymic: PersonFields.patronymic
    gender: PersonFields.gender
    birth_date: PersonFields.birth_date


class PersonSchemaGET(PersonSchema):
    pass


class PersonSchemaPOST(BaseModelForSchema):
    name: PersonFields.name
    surname: PersonFields.surname
    patronymic: PersonFields.patronymic
    gender: PersonFields.gender
    birth_date: PersonFields.birth_date
