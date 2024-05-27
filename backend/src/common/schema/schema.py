from datetime import datetime
from typing import ClassVar
from uuid import uuid4

from pydantic import Field
from pydantic.v1.fields import UndefinedType

from ..schema import BaseFields
from ..schema import BaseSchemaConfig
from ..schema.fields import TZ_UTC


class BaseSchema(BaseSchemaConfig):
    id: BaseFields.id = Field(
        default_factory=lambda: uuid4(),
    )
    created_at: BaseFields.created_at = Field(
        default_factory=lambda: datetime.now(TZ_UTC),
    )
    updated_at: BaseFields.updated_at = Field(
        default_factory=lambda: datetime.now(TZ_UTC),
    )


class BaseSchemaPOST(BaseSchema):
    id: ClassVar[UndefinedType]  # type:ignore
    created_at: ClassVar[UndefinedType]  # type:ignore
    updated_at: ClassVar[UndefinedType]  # type:ignore
