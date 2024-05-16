from pydantic import BaseModel
from pydantic import ConfigDict

from .fields import BaseSchemaFields


class BaseModelForSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)


class BaseSchema(BaseModelForSchema):
    id: BaseSchemaFields.id_field
    created_at: BaseSchemaFields.created_at_field
    updated_at: BaseSchemaFields.updated_at_field
