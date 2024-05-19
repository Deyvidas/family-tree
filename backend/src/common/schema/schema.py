from .config import BaseModelForSchema
from .fields import BaseFields


class BaseSchema(BaseModelForSchema):
    id: BaseFields.id
    created_at: BaseFields.created_at
    updated_at: BaseFields.updated_at
