from ..repository import RepositoryInterface
from ..schema import Schema
from ..schema import SchemaGET
from ..schema import SchemaPOST


class Service:
    def __init__(self, repository: RepositoryInterface):
        self._repository = repository

    def create(
        self,
        data: SchemaPOST,
    ) -> SchemaGET:
        new_data = Schema(**data.model_dump())
        created = self._repository.create(new_data)
        return SchemaGET.model_validate(created)
