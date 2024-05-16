from datetime import datetime
from typing import Annotated

from pydantic import Field


class BaseSchemaFields:
    id_field = Annotated[
        str,
        Field(),
    ]
    created_at_field = Annotated[
        datetime,
        Field(),
    ]
    updated_at_field = Annotated[
        datetime,
        Field(),
    ]
