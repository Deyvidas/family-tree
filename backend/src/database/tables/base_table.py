from datetime import datetime
from datetime import timedelta
from datetime import timezone
from typing import Annotated
from uuid import uuid4

from sqlalchemy import DateTime
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column


datetimeTZ = Annotated[datetime, mapped_column(DateTime(timezone=True))]
timezoneUTC = timezone(timedelta())


class BaseTable(DeclarativeBase):
    id: Mapped[str] = mapped_column(
        primary_key=True,
        default=lambda: uuid4().hex,
    )
    created_at: Mapped[datetimeTZ] = mapped_column(
        default=lambda: datetime.now(timezoneUTC),
    )
    updated_at: Mapped[datetimeTZ] = mapped_column(
        default=lambda: datetime.now(timezoneUTC),
        onupdate=lambda: datetime.now(timezoneUTC),
    )

    show_fields = ['id']

    def __repr__(self) -> str:
        name = type(self).__name__
        values = [f'{f}: {repr(getattr(self, f))}' for f in self.show_fields]
        return f'{name}({', '.join(values)})'
