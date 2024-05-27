from abc import ABC
from abc import abstractmethod
from typing import TypeVar

from ..schema import Schema


TSchema = TypeVar('TSchema')


class RepositoryInterface(ABC):
    @abstractmethod
    def create(
        self,
        data: Schema,
    ) -> Schema:
        """
        Add new personal information about the person to the database
        """
        raise NotImplementedError
