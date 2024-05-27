from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from .base import BaseTable


if TYPE_CHECKING:
    from .person import PersonTable


class BiographyTable(BaseTable):
    __tablename__ = 'biography'

    birth_place: Mapped[str]
    profession: Mapped[str]
    history: Mapped[str]
    company: Mapped[str]
    interest: Mapped[str]

    person_id: Mapped[str] = mapped_column(
        ForeignKey('person.id', ondelete='CASCADE'),
    )
    person: Mapped['PersonTable'] = relationship(
        lazy='joined',
        back_populates='biography',
    )
