from datetime import date
from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from src.database.tables import BaseTable


if TYPE_CHECKING:
    from .person import PersonTable


class PersonalInfoTable(BaseTable):
    __tablename__ = 'personal_info'

    name: Mapped[str]
    surname: Mapped[str]
    surname_at_birth: Mapped[str]
    patronymic: Mapped[str]
    gender: Mapped[str]
    birth_date: Mapped[date]
    dead_date: Mapped[date]

    person_id: Mapped[str] = mapped_column(
        ForeignKey('person.id', ondelete='CASCADE'),
    )
    person: Mapped['PersonTable'] = relationship(
        lazy='joined',
        back_populates='personal_info',
    )
