from pydantic import BaseModel

from src.schemas.base import BaseSchema


class PersonSchemaGET(BaseSchema):
    first_name: str
    last_name: str


class PersonSchemaPOST(BaseModel):
    first_name: str
    last_name: str
