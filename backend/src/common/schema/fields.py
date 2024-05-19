from datetime import datetime
from typing import Annotated

from pydantic import Field


class BaseFields:
    id = Annotated[
        str,
        Field(),
    ]
    created_at = Annotated[
        datetime,
        Field(),
    ]
    updated_at = Annotated[
        datetime,
        Field(),
    ]

    optional = Field(
        default=None,
    )
