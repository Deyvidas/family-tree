from src.common.exceptions import ServiceErrorMoreThanOneFound
from src.common.exceptions import ServiceErrorNotFound
from src.database import DatabaseConfig

from .person_repository import PersonRepository
from .schema.person_filter import PersonFilterFULL
from .schema.person_schema import PersonSchemaFULL
from .schema.person_schema import PersonSchemaPOST


class PersonService:
    repository = PersonRepository(DatabaseConfig.main_config.sessionmaker)

    def get_all(self) -> list[PersonSchemaFULL]:
        people_list = self.repository.filter()
        return people_list

    def get_strict_one(self, filters: PersonFilterFULL) -> PersonSchemaFULL:
        founded_people = self.filter_by(filters)
        params = f'params={filters.model_dump()}'

        if len(founded_people) == 1:
            return founded_people[0]
        elif len(founded_people) == 0:
            msg = f'Person with {params} not found.'
            raise ServiceErrorNotFound(msg)
        else:
            msg = f'Found more than 1 person with {params}'
            raise ServiceErrorMoreThanOneFound(msg)

    def filter_by(self, filters: PersonFilterFULL) -> list[PersonSchemaFULL]:
        filtered_people = self.repository.filter(**filters.model_dump())
        return filtered_people

    def create_person(self, person_data: PersonSchemaPOST) -> PersonSchemaFULL:
        new_person = self.repository.create(**person_data.model_dump())
        return new_person
