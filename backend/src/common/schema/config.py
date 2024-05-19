from __future__ import annotations

from typing import Any
from typing import Literal
from typing import NotRequired
from typing import Self
from typing import TypedDict
from typing import Unpack

from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic.main import IncEx

from src.common.exceptions import SchemaDoesNotHaveFields


class BaseModelForSchema(BaseModel):
    @classmethod
    def model_validate_many(
        cls,
        objects: list[Any],
        **options: Unpack[ModelValidateOptions],
    ) -> list[Self]:
        return [cls.model_validate(obj, **options) for obj in objects]

    @classmethod
    def model_dump_many(
        cls,
        objects: list[Self],
        **options: Unpack[ModelDumpOptions],
    ) -> list[dict[str, Any]]:
        return [obj.model_dump(**options) for obj in objects]

    @classmethod
    def has_fields(
        cls,
        fields: list[str],
    ) -> None:
        """
        Check if the passed fields are present in the schema. If at least one
        field is missing from the schema, raise a SchemaDoesNotHaveFields
        exception
        """

        extra_fields = set(fields) - set(cls.model_fields.keys())
        if len(extra_fields) == 0:
            return

        msg = f'Schema {cls.__name__} does not have fields {fields}'
        raise SchemaDoesNotHaveFields(msg)

    model_config = ConfigDict(
        from_attributes=True,
        use_enum_values=True,
    )


class ModelValidateOptions(TypedDict):
    """Arguments of BaseModel.model_validate()"""

    strict: NotRequired[bool]
    from_attributes: NotRequired[bool]
    context: NotRequired[dict[str, Any]]


class ModelDumpOptions(TypedDict):
    """Arguments of BaseModel.model_dump()"""

    mode: NotRequired[str]
    include: NotRequired[IncEx]
    exclude: NotRequired[IncEx]
    context: NotRequired[dict[str, Any]]
    by_alias: NotRequired[bool]
    exclude_unset: NotRequired[bool]
    exclude_defaults: NotRequired[bool]
    exclude_none: NotRequired[bool]
    round_trip: NotRequired[bool]
    warnings: NotRequired[bool | Literal['none', 'warn', 'error']]
    serialize_as_any: NotRequired[bool]
