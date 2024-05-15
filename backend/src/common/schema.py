from datetime import datetime

from pydantic import BaseModel
from pydantic import ConfigDict


class BaseSchema(BaseModel):
    id: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)
