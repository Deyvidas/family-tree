from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import relationship

from .base import BaseTable


if TYPE_CHECKING:
    from .biography import BiographyTable
    from .contact import ContactTable
    from .personal_info import PersonalInfoTable


class PersonTable(BaseTable):
    __tablename__ = 'person'

    biography: Mapped['BiographyTable'] = relationship(
        lazy='joined',
        back_populates='person',
    )
    contact: Mapped['ContactTable'] = relationship(
        lazy='joined',
        back_populates='person',
    )
    personal_info: Mapped['PersonalInfoTable'] = relationship(
        lazy='joined',
        back_populates='person',
    )
