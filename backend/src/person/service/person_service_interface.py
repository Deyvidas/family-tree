from abc import ABC
from abc import abstractmethod

from .person_service_dto import PersonSchemaGET
from .person_service_dto import PersonSchemaPOST


class PersonServiceInterface(ABC):
    @abstractmethod
    def get_all(
        self,
        order_by: list[str],
    ) -> list[PersonSchemaGET]:
        raise NotImplementedError()

    @abstractmethod
    def create_person(
        self,
        data: PersonSchemaPOST,
    ) -> PersonSchemaGET:
        raise NotImplementedError()
