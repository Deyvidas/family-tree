from abc import ABC
from abc import abstractmethod
from typing import Any

from sqlalchemy.orm import Session
from sqlalchemy.orm import sessionmaker

from .schema.schema import BaseSchema


class BaseRepository[T: BaseSchema](ABC):
    schema: type[T]

    def __init__(self, sessionmaker: sessionmaker[Session]):
        self.sessionmaker = sessionmaker

    @abstractmethod
    def create(self, **kwargs) -> T:
        raise NotImplementedError()

    @abstractmethod
    def bulk_create(self, kwargs_list: list[dict[str, Any]]) -> list[T]:
        raise NotImplementedError()

    @abstractmethod
    def filter(self, **kwargs) -> list[T]:
        raise NotImplementedError()
