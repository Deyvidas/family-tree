from abc import ABC
from abc import abstractmethod

from src.common.types import OrderBy
from src.person.schema.person_schema import PersonSchema
from src.person.schema.person_schema import PersonSchemaPOST


class PersonServiceInterface(ABC):
    @abstractmethod
    def get_all(
        self,
        order_by: list[OrderBy],
    ) -> list[PersonSchema]:
        raise NotImplementedError()

    @abstractmethod
    def create_person(
        self,
        data: PersonSchemaPOST,
    ) -> PersonSchema:
        raise NotImplementedError()
