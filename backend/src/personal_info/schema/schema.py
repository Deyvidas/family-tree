from src.common.schema import BaseSchema
from src.common.schema import BaseSchemaConfig
from src.person.schema.fields import Fields as PersonFields

from .fields import Fields


class TSchema(BaseSchemaConfig):
    name: Fields.name
    surname: Fields.surname
    surname_at_birth: Fields.surname_at_birth
    patronymic: Fields.patronymic
    gender: Fields.gender
    birth_date: Fields.birth_date
    dead_date: Fields.dead_date


class Schema(TSchema, BaseSchema):
    person_id: PersonFields.id


class SchemaGET(TSchema, BaseSchema):
    person_id: PersonFields.id


class SchemaGETRef(TSchema, BaseSchema):
    pass


class SchemaPOST(TSchema):
    person_id: PersonFields.id


class SchemaPOSTRef(TSchema):
    pass
