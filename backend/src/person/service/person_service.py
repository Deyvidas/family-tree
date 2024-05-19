from typing import override

from src.common.types import OrderBy
from src.person.repository.person_repository import PersonRepositories
from src.person.repository.person_repository import PersonRepository
from src.person.schema.person_schema import PersonSchema
from src.person.schema.person_schema import PersonSchemaPOST

from .person_service_interface import PersonServiceInterface


class PersonService(PersonServiceInterface):
    def __init__(
        self,
        repository: PersonRepository,
    ):
        self.repository = repository

    @override
    def get_all(
        self,
        order_by: list[OrderBy],
    ) -> list[PersonSchema]:
        return self.repository.filter(order_by=order_by)

    @override
    def create_person(
        self,
        data: PersonSchemaPOST,
    ) -> PersonSchema:
        return self.repository.create(data)


class PersonServices:
    main_service = PersonService(
        repository=PersonRepositories.sqlalchemy_main,
    )
    test_service = PersonService(
        repository=PersonRepositories.sqlalchemy_test,
    )
