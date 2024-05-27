from typing import Annotated

from pydantic import Field

from src.common.schema import BaseFields


class Fields(BaseFields):
    birth_place = Annotated[
        str,
        Field(),
    ]
    profession = Annotated[
        str,
        Field(),
    ]
    history = Annotated[
        str,
        Field(),
    ]
    company = Annotated[
        str,
        Field(),
    ]
    interest = Annotated[
        str,
        Field(),
    ]
