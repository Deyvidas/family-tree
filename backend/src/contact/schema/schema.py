from typing import ClassVar

from pydantic.v1.fields import UndefinedType

from src.common.schema import BaseSchema
from src.common.schema import BaseSchemaPOST
from src.person.schema.fields import Fields as PersonFields

from .fields import Fields


class Schema(BaseSchema):
    person_id: PersonFields.id

    email: Fields.email
    home_phone: Fields.home_phone
    mobile_phone: Fields.mobile_phone
    address: Fields.address


class SchemaGET(Schema):
    pass


class SchemaGETRef(Schema):
    person_id: ClassVar[UndefinedType]  # type: ignore


class SchemaPOST(Schema, BaseSchemaPOST):
    pass


class SchemaPOSTRef(Schema, BaseSchemaPOST):
    person_id: ClassVar[UndefinedType]  # type: ignore
