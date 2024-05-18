from abc import ABC
from abc import abstractmethod
from typing import Any

from src.person.schema.person_schema import PersonSchema

from .person_repository_dto import PersonSchemaInsert


class PersonRepositoryInterface(ABC):
    @abstractmethod
    def create(
        self,
        data: PersonSchemaInsert,
    ) -> PersonSchema:
        raise NotImplementedError()

    @abstractmethod
    def bulk_create(
        self,
        data_list: list[PersonSchemaInsert],
    ) -> list[PersonSchema]:
        raise NotImplementedError()

    @abstractmethod
    def filter(
        self,
        filter_by: dict[str, Any] | None = None,
        order_by: list[str] | None = None,
    ) -> list[PersonSchema]:
        raise NotImplementedError()
