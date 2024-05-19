from typing import Any
from typing import override

from sqlalchemy import Select
from sqlalchemy import insert
from sqlalchemy import select
from sqlalchemy.orm import InstrumentedAttribute
from sqlalchemy.orm import Session
from sqlalchemy.orm import sessionmaker as sqlalchemy_sessionmaker

from src.common.types import OrderBy
from src.database import DatabaseConfig
from src.database.tables.person_table import PersonTable
from src.person.schema.person_schema import PersonSchema
from src.person.schema.person_schema import PersonSchemaPOST

from .person_repository_interface import PersonRepositoryInterface


class PersonRepository(PersonRepositoryInterface):
    table = PersonTable

    def __init__(
        self,
        sessionmaker: sqlalchemy_sessionmaker[Session],
    ):
        self.sessionmaker = sessionmaker

    @override
    def create(
        self,
        data: PersonSchemaPOST,
    ) -> PersonSchema:
        query = (
            insert(self.table)
            .values(**data.model_dump())
            .returning(self.table)
        )

        with self.sessionmaker() as session:
            new_entity = session.scalars(query).one()
            session.commit()
            return PersonSchema.model_validate(new_entity)

    @override
    def bulk_create(
        self,
        data_list: list[PersonSchemaPOST],
    ) -> list[PersonSchema]:
        query = (
            insert(self.table)
            .values(PersonSchemaPOST.model_dump_many(data_list))
            .returning(self.table)
        )

        with self.sessionmaker() as session:
            new_entities = list(session.scalars(query).all())
            session.commit()
            return PersonSchema.model_validate_many(new_entities)

    @override
    def filter(
        self,
        filter_by: dict[str, Any] | None = None,
        order_by: list[OrderBy] | None = None,
    ) -> list[PersonSchema]:
        query = select(self.table)
        query = self.__enrich_select_filter_by(query, filter_by)
        query = self.__enrich_select_order_by(query, order_by)

        with self.sessionmaker() as session:
            filtered_entities = list(session.scalars(query).all())
            return PersonSchema.model_validate_many(filtered_entities)

    def __enrich_select_filter_by(
        self,
        select_stmt: Select[tuple[PersonTable]],
        filter_by: dict[str, Any] | None,
    ) -> Select[tuple[PersonTable]]:
        if filter_by is None:
            return select_stmt

        PersonSchema.has_fields(list(filter_by))

        select_stmt = select_stmt.filter_by(**filter_by)
        return select_stmt

    def __enrich_select_order_by(
        self,
        select_stmt: Select[tuple[PersonTable]],
        order_by: list[OrderBy] | None,
    ) -> Select[tuple[PersonTable]]:
        if order_by is None:
            return select_stmt

        PersonSchema.has_fields([order.field for order in order_by])

        for order in order_by:
            column: InstrumentedAttribute[Any] = getattr(
                PersonTable, order.field
            )
            match order.direction:
                case 'asc':
                    select_stmt = select_stmt.order_by(column.asc())
                case 'desc':
                    select_stmt = select_stmt.order_by(column.desc())

        return select_stmt


class PersonRepositories:
    sqlalchemy_main = PersonRepository(
        sessionmaker=DatabaseConfig.main_config.sessionmaker,
    )
    sqlalchemy_test = PersonRepository(
        sessionmaker=DatabaseConfig.test_config.sessionmaker,
    )
