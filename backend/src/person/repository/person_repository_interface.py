from abc import ABC
from abc import abstractmethod
from typing import Any

from src.common.types import OrderBy
from src.person.schema.person_schema import PersonSchema
from src.person.schema.person_schema import PersonSchemaPOST


class PersonRepositoryInterface(ABC):
    @abstractmethod
    def create(
        self,
        data: PersonSchemaPOST,
    ) -> PersonSchema:
        raise NotImplementedError()

    @abstractmethod
    def bulk_create(
        self,
        data_list: list[PersonSchemaPOST],
    ) -> list[PersonSchema]:
        raise NotImplementedError()

    @abstractmethod
    def filter(
        self,
        filter_by: dict[str, Any] | None = None,
        order_by: list[OrderBy] | None = None,
    ) -> list[PersonSchema]:
        raise NotImplementedError()
