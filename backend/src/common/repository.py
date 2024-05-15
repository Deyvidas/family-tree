from abc import ABC
from abc import abstractmethod

from sqlalchemy.orm import Session
from sqlalchemy.orm import sessionmaker

from .schema import BaseSchema


class BaseRepository[T: BaseSchema](ABC):
    schema: type[T]

    def __init__(self, sessionmaker: sessionmaker[Session]):
        self.sessionmaker = sessionmaker

    @abstractmethod
    def get(self) -> T:
        raise NotImplementedError()

    @abstractmethod
    def filter(self, **kwargs) -> list[T]:
        raise NotImplementedError()

    @abstractmethod
    def create(self, **kwargs) -> T:
        raise NotImplementedError()
