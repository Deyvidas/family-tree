from src.common.schema.schema import BaseModelForSchema
from src.common.schema.schema import BaseSchema

from .person_fields import PersonSchemaFields


class PersonSchema(BaseModelForSchema):
    name: PersonSchemaFields.name
    surname: PersonSchemaFields.surname
    patronymic: PersonSchemaFields.patronymic
    gender: PersonSchemaFields.gender
    birth_date: PersonSchemaFields.birth_date


class PersonSchemaFULL(BaseSchema, PersonSchema):
    pass


class PersonSchemaPOST(PersonSchema):
    pass
