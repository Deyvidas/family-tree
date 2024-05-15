from fastapi import APIRouter

from src.person.person_schema import PersonSchema
from src.person.person_schema import PersonSchemaPOST
from src.person.person_service import PersonService


router = APIRouter()
service = PersonService()


@router.get(
    summary='Get all available person.',
    path='/',
    response_model=list[PersonSchema],
)
def get_all_people():
    return service.get_all()


@router.post(
    summary='Create a new person',
    path='/',
    response_model=PersonSchema,
)
def create_person(user: PersonSchemaPOST):
    return service.create_person(user)
