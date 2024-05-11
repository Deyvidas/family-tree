from datetime import date
from enum import Enum

from sqlalchemy.orm import Mapped

from src.tables import BaseTable


class EnumGender(Enum):
    male = 'male'
    female = 'female'


class PersonTable(BaseTable):
    __tablename__ = 'person'

    name: Mapped[str]
    surname: Mapped[str]
    patronymic: Mapped[str]
    gender: Mapped[EnumGender]
    birth_date: Mapped[date]

    show_fields = ['name', 'surname', 'birth_date']
