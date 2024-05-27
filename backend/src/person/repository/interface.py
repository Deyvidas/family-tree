from abc import ABC

from ..schema import Schema


class RepositoryInterface(ABC):
    def create(self, data: Schema) -> Schema:
        pass
