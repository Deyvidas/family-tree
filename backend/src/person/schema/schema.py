from src import biography
from src import contact
from src import personal_info
from src.common.schema import BaseSchema
from src.common.schema import BaseSchemaPOST


class TSchema(BaseSchema):
    personal_info: personal_info.SchemaGETRef
    contact: contact.SchemaGETRef
    biography: biography.SchemaGETRef


class Schema(TSchema):
    pass


class SchemaGET(TSchema):
    pass


class SchemaPOST(BaseSchemaPOST):
    personal_info: personal_info.SchemaPOSTRef
    contact: contact.SchemaPOSTRef
    biography: biography.SchemaPOSTRef
