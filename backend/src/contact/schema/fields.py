from typing import Annotated

from pydantic import Field

from src.common.schema import BaseFields


class Fields(BaseFields):
    email = Annotated[
        str,
        Field(),
    ]
    home_phone = Annotated[
        str,
        Field(),
    ]
    mobile_phone = Annotated[
        str,
        Field(),
    ]
    address = Annotated[
        str,
        Field(),
    ]
