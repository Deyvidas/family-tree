from datetime import date

from sqlalchemy.orm import Mapped

from .base_table import BaseTable


class PersonTable(BaseTable):
    __tablename__ = 'person'

    name: Mapped[str]
    surname: Mapped[str]
    patronymic: Mapped[str]
    gender: Mapped[str]
    birth_date: Mapped[date]

    show_fields = ['name', 'surname', 'birth_date']
