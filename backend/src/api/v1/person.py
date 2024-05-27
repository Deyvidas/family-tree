from typing import Annotated

from fastapi import APIRouter
from fastapi import Depends

from src import person


def get_person_service() -> person.Service:
    return person.service


router = APIRouter()
ServiceDepends = Annotated[person.Service, Depends(get_person_service)]


@router.get(
    summary='Get all people',
    path='/',
)
def get_all_people(service: ServiceDepends) -> list[person.SchemaGET]:
    return service.get_all()


@router.post(
    summary='Create a new person',
    path='/',
)
def create_new_person(
    data: person.SchemaPOST,
    service: ServiceDepends,
) -> person.SchemaGET:
    return service.create_person(data)
