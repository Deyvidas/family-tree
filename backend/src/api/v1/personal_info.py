from typing import Annotated

from fastapi import APIRouter
from fastapi import Depends

from src.personal_info.repository import RepositorySqlalchemy
from src.personal_info.schema import SchemaGET
from src.personal_info.schema import SchemaPOST
from src.personal_info.service import Service


def get_personal_info_service() -> Service:
    return Service(RepositorySqlalchemy())


router = APIRouter()
ServiceDepends = Annotated[
    Service,
    Depends(get_personal_info_service),
]


@router.post(
    summary='Create new personal info about person',
    path='/',
    response_model=SchemaGET,
)
def create_personal_info(
    data: SchemaPOST,
    service: ServiceDepends,
) -> SchemaGET:
    return service.create(data)
