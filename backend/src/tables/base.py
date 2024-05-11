from datetime import datetime
from uuid import uuid4

from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import declared_attr
from sqlalchemy.orm import mapped_column


class BaseTable(DeclarativeBase):
    id: Mapped[str] = mapped_column(
        primary_key=True,
        default=lambda: uuid4().hex,
    )
    created_at: Mapped[datetime] = mapped_column(
        default=lambda: datetime.now(),
    )
    updated_at: Mapped[datetime | None] = mapped_column(
        onupdate=lambda: datetime.now(),
    )

    show_fields = ['id']

    @declared_attr.directive
    def __tablename__(cls) -> str:
        return cls.__name__.lower().replace('table', '')

    def __repr__(self) -> str:
        name = type(self).__name__.replace('Table', '')
        values = [f'{f}: {repr(getattr(self, f))}' for f in self.show_fields]
        return f'{name}({', '.join(values)})'
