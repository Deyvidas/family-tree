from abc import ABC
from abc import abstractmethod
from typing import Any

from src.common.types import OrderBy

from ..schema import Schema


class RepositoryInterface(ABC):
    @abstractmethod
    def create(
        self,
        data: Schema,
    ) -> Schema:
        """
        Create the interest in the repository and return it
        """
        raise NotImplementedError

    @abstractmethod
    def bulk_create(
        self,
        data_list: list[Schema],
    ) -> list[Schema]:
        """
        Create more than one interest in the repository and return them
        """
        raise NotImplementedError

    @abstractmethod
    def filter(
        self,
        filter_by: dict[str, Any] | None = None,
        order_by: list[OrderBy] | None = None,
    ) -> list[Schema]:
        """
        Find all interests ordered by order_by from the repository that match
        the filters
        """
        raise NotImplementedError
