from typing import Annotated

from pydantic import Field

from src.common.schema import BaseFields


class Fields(BaseFields):
    name = Annotated[
        str,
        Field(),
    ]
    description = Annotated[
        str,
        Field(),
    ]
