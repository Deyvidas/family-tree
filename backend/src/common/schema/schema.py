from .fields import BaseFields
from .config import BaseModelForSchema


class BaseSchema(BaseModelForSchema):
    id: BaseFields.id
    created_at: BaseFields.created_at
    updated_at: BaseFields.updated_at
