from typing import Annotated

from fastapi import APIRouter
from fastapi import Depends
from fastapi import status

from src.interest.repository import RepositorySqlalchemy
from src.interest.schema import SchemaGET
from src.interest.schema import SchemaPOST
from src.interest.service import Service


def get_interest_service() -> Service:
    return Service(RepositorySqlalchemy())


router = APIRouter()
ServiceDepends = Annotated[Service, Depends(get_interest_service)]


@router.get(
    summary='Return all interests',
    path='/',
    response_model=list[SchemaGET],
)
def get_all_interests(service: ServiceDepends) -> list[SchemaGET]:
    return service.get_all()


@router.post(
    summary='Create a new interest',
    path='/',
    response_model=SchemaGET,
    status_code=status.HTTP_201_CREATED,
)
def create_one_interest(
    data: SchemaPOST,
    service: ServiceDepends,
) -> SchemaGET:
    return service.create(data)
