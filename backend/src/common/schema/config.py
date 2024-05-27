from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import TypeAdapter


class BaseSchemaConfig(BaseModel):
    @classmethod
    def many(cls):
        return TypeAdapter(list[cls])

    model_config = ConfigDict(
        from_attributes=True,
        use_enum_values=True,
        validate_assignment=True,
    )
