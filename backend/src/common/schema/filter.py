from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import Field

from .fields import BaseSchemaFields


class BaseModelForFilter(BaseModel):
    model_config = ConfigDict()


class BaseFilter(BaseModelForFilter):
    """All fields that can be used to filter rows in the repository."""

    id: BaseSchemaFields.id_field = Field(default=None)
    created_at: BaseSchemaFields.created_at_field = Field(default=None)
    updated_at: BaseSchemaFields.updated_at_field = Field(default=None)
