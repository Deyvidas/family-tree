from typing import Literal
from typing import NamedTuple


class OrderBy(NamedTuple):
    field: str
    direction: Literal['asc', 'desc']
