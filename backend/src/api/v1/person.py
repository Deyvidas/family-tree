from fastapi import APIRouter

from src.person.service.person_service import PersonServices
from src.person.service.person_service_dto import PersonSchemaGET
from src.person.service.person_service_dto import PersonSchemaPOST


router = APIRouter()
service = PersonServices.main_service


@router.get(
    summary='Get all available person.',
    path='/',
    response_model=list[PersonSchemaGET],
)
def get_all_people():
    return service.get_all(order_by=['-updated_at'])


@router.post(
    summary='Create a new person',
    path='/',
    response_model=PersonSchemaGET,
)
def create_person(user: PersonSchemaPOST):
    return service.create_person(user)
