from typing import Any
from typing import override

from sqlalchemy import insert
from sqlalchemy import select

from src.common.repository import BaseRepository
from src.database.tables import PersonTable

from .schema.person_schema import PersonSchemaFULL


class PersonRepository(BaseRepository[PersonSchemaFULL]):
    table = PersonTable
    schema = PersonSchemaFULL

    @override
    def create(self, **kwargs) -> PersonSchemaFULL:
        stmt = insert(self.table).values(**kwargs).returning(self.table)
        with self.sessionmaker() as session:
            new_person = session.scalars(stmt).one()
            session.commit()
            return self.schema.model_validate(new_person)

    @override
    def bulk_create(
        self,
        kwargs_list: list[dict[str, Any]],
    ) -> list[PersonSchemaFULL]:
        stmt = insert(self.table).values(kwargs_list).returning(self.table)
        with self.sessionmaker() as session:
            new_people = list(session.scalars(stmt).all())
            session.commit()
            return self.schema.model_validate_many(new_people)

    @override
    def filter(self, **kwargs) -> list[PersonSchemaFULL]:
        stmt = select(self.table).filter_by(**kwargs)
        with self.sessionmaker() as session:
            people_list = list(session.scalars(stmt).all())
            return self.schema.model_validate_many(people_list)
