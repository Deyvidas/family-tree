from src.database import DatabaseConfig

from .person_repository import PersonRepository
from .person_schema import PersonSchema
from .person_schema import PersonSchemaPOST


class PersonService:
    repository = PersonRepository(DatabaseConfig.main_config.sessionmaker)

    def get_all(self) -> list[PersonSchema]:
        people_list = self.repository.filter()
        return people_list

    def create_person(self, person_data: PersonSchemaPOST) -> PersonSchema:
        new_person = self.repository.create(**person_data.model_dump())
        return new_person
