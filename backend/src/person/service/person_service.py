from typing import override

from src.person.repository.person_repository import PersonRepositories
from src.person.repository.person_repository import PersonRepository
from src.person.repository.person_repository_dto import PersonSchemaInsert
from src.person.service.person_service_dto import PersonSchemaGET
from src.person.service.person_service_dto import PersonSchemaPOST

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
        order_by: list[str],
    ) -> list[PersonSchemaGET]:
        filtered_people = self.repository.filter(order_by=order_by)
        return PersonSchemaGET.model_validate_many(filtered_people)

    @override
    def create_person(
        self,
        data: PersonSchemaPOST,
    ) -> PersonSchemaGET:
        insert_data = PersonSchemaInsert.model_validate(data)
        new_person = self.repository.create(insert_data)
        return PersonSchemaGET.model_validate(new_person)


class PersonServices:
    main_service = PersonService(
        repository=PersonRepositories.sqlalchemy_main,
    )
    test_service = PersonService(
        repository=PersonRepositories.sqlalchemy_test,
    )
