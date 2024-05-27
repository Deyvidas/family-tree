from sqlalchemy.orm import Mapped

from .base import BaseTable


class InterestTable(BaseTable):
    __tablename__ = 'interest'

    name: Mapped[str]
    description: Mapped[str]
