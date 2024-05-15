from sqlalchemy import insert
from sqlalchemy import select

from src.common.exceptions import MoreThanOneFoundError
from src.common.exceptions import NotFoundError
from src.common.repository import BaseRepository
from src.database.tables import PersonTable

from .person_schema import PersonSchema


class PersonRepository(BaseRepository[PersonSchema]):
    table = PersonTable
    schema = PersonSchema

    def create(self, **kwargs) -> PersonSchema:
        stmt = insert(self.table).values(**kwargs).returning(self.table)
        with self.sessionmaker() as session:
            new_person = session.scalars(stmt).one()
            session.commit()
            return self.schema.model_validate(new_person)

    def get(self, **kwargs) -> PersonSchema:
        person = self.filter(**kwargs)
        if len(person) == 1:
            return person[0]
        elif len(person) == 0:
            raise NotFoundError('Person not found')
        else:
            raise MoreThanOneFoundError('Found more than 1 person')

    def filter(self, **kwargs) -> list[PersonSchema]:
        stmt = select(self.table).filter_by(**kwargs)
        with self.sessionmaker() as session:
            people_list = list(session.scalars(stmt).all())
            return [self.schema.model_validate(p) for p in people_list]
