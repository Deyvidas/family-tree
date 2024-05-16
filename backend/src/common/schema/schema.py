from typing import Any
from typing import Self

from pydantic import BaseModel
from pydantic import ConfigDict

from .fields import BaseSchemaFields


class BaseModelForSchema(BaseModel):
    @classmethod
    def model_validate_many(cls, objects: list[Any]) -> list[Self]:
        return [cls.model_validate(obj) for obj in objects]

    model_config = ConfigDict(from_attributes=True)


class BaseSchema(BaseModelForSchema):
    id: BaseSchemaFields.id_field
    created_at: BaseSchemaFields.created_at_field
    updated_at: BaseSchemaFields.updated_at_field
