from datetime import datetime

from pydantic import BaseModel


class BaseSchema(BaseModel):
    id: str
    created_at: datetime
    updated_at: datetime | None
