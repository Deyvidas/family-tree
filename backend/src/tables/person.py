from sqlalchemy.orm import Mapped

from src.tables import BaseTable


class PersonTable(BaseTable):
    first_name: Mapped[str]
    last_name: Mapped[str]

    show_fields = ['first_name', 'last_name']
