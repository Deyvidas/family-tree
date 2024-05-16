from fastapi import APIRouter

from src.person.person_service import PersonService
from src.person.schema.person_schema import PersonSchemaFULL
from src.person.schema.person_schema import PersonSchemaPOST


router = APIRouter()
service = PersonService()


@router.get(
    summary='Get all available person.',
    path='/',
    response_model=list[PersonSchemaFULL],
)
def get_all_people():
    return service.get_all()


@router.post(
    summary='Create a new person',
    path='/',
    response_model=PersonSchemaFULL,
)
def create_person(user: PersonSchemaPOST):
    return service.create_person(user)
