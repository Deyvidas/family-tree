from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from .base import BaseTable


if TYPE_CHECKING:
    from .person import PersonTable


class ContactTable(BaseTable):
    __tablename__ = 'contact'

    email: Mapped[str]
    home_phone: Mapped[str]
    mobile_phone: Mapped[str]
    address: Mapped[str]

    person_id: Mapped[str] = mapped_column(
        ForeignKey('person.id', ondelete='CASCADE'),
    )
    person: Mapped['PersonTable'] = relationship(
        lazy='joined',
        back_populates='contact',
    )
