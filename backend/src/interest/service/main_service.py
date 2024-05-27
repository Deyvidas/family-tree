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
        new_interest_data = Schema.model_validate(data)
        new_interest = self._repository.create(new_interest_data)
        return SchemaGET.model_validate(new_interest)

    def get_all(self) -> list[SchemaGET]:
        interests_list = self._repository.filter()
        return SchemaGET.many().validate_python(interests_list)
