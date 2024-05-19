from fastapi import APIRouter

from src.common.types import OrderBy
from src.person.schema.person_schema import PersonSchemaGET
from src.person.schema.person_schema import PersonSchemaPOST
from src.person.service.person_service import PersonServices


router = APIRouter()
service = PersonServices.main_service


@router.get(
    summary='Get all available people',
    path='/',
    response_model=list[PersonSchemaGET],
)
def get_all_people() -> list[PersonSchemaGET]:
    people = service.get_all(order_by=[OrderBy('updated_at', 'desc')])
    return PersonSchemaGET.model_validate_many(people)


@router.post(
    summary='Create a new person',
    path='/',
    response_model=PersonSchemaGET,
)
def create_person(person: PersonSchemaPOST) -> PersonSchemaGET:
    new_person = service.create_person(person)
    return PersonSchemaGET.model_validate(new_person)
