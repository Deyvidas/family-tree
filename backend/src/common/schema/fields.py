from datetime import datetime
from datetime import timedelta
from datetime import timezone
from typing import Annotated

from pydantic import UUID4
from pydantic import Field


TZ_UTC = timezone(offset=timedelta(), name='UTC')


class BaseFields:
    id = Annotated[
        UUID4,
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
