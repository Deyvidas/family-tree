from src.common.schema import BaseSchema
from src.common.schema import BaseSchemaPOST

from .fields import Fields


class Schema(BaseSchema):
    name: Fields.name
    description: Fields.description


class SchemaGET(Schema):
    pass


class SchemaPOST(Schema, BaseSchemaPOST):
    pass
