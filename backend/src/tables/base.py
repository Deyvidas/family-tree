from datetime import datetime
from typing import Annotated
from uuid import uuid4

from sqlalchemy import DateTime
from sqlalchemy import func
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column


datetimeTZ = Annotated[datetime, mapped_column(DateTime(timezone=True))]


class BaseTable(DeclarativeBase):
    id: Mapped[str] = mapped_column(
        primary_key=True,
        default=lambda: uuid4().hex,
    )
    created_at: Mapped[datetimeTZ] = mapped_column(
        server_default=func.now(),
    )
    updated_at: Mapped[datetimeTZ | None] = mapped_column(
        onupdate=func.now(),
    )

    show_fields = ['id']

    def __repr__(self) -> str:
        name = type(self).__name__
        values = [f'{f}: {repr(getattr(self, f))}' for f in self.show_fields]
        return f'{name}({', '.join(values)})'
