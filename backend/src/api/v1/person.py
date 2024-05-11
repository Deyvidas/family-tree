from fastapi import APIRouter

from src.repo.person import PersonRepo
from src.schemas.person import PersonSchemaGET
from src.schemas.person import PersonSchemaPOST


router = APIRouter(prefix='/person')
repo = PersonRepo()


@router.get(
    path='',
    response_model=list[PersonSchemaGET],
)
def get_users():
    return repo.get_all()


@router.post(
    path='',
    response_model=PersonSchemaGET,
)
def create_user(user: PersonSchemaPOST):
    return repo.create_user(**user.model_dump())
