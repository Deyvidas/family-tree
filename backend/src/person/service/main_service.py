from src import personal_info

from ..repository import RepositoryInterface
from ..schema import SchemaGET
from ..schema import SchemaPOST


class Service:
    def __init__(
        self,
        repository: RepositoryInterface,
    ):
        self._repository = repository

    def create_person(
        self,
        data: SchemaPOST,
    ):
        personal_info.service.create(data.personal_info)
        pass

    def get_all(self) -> list[SchemaGET]:
        pass
