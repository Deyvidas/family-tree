from typing import Any
from typing import override

from sqlalchemy import Select
from sqlalchemy import insert
from sqlalchemy import select
from sqlalchemy.orm import InstrumentedAttribute
from sqlalchemy.orm import Session
from sqlalchemy.orm import sessionmaker as sqlalchemy_sessionmaker

from src.common.repository.exceptions import RepositoryErrorUnexistentColumn
from src.database import DatabaseConfig
from src.database.tables.person_table import PersonTable
from src.person.schema.person_schema import PersonSchema

from .person_repository_dto import PersonSchemaInsert
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
        data: PersonSchemaInsert,
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
        data_list: list[PersonSchemaInsert],
    ) -> list[PersonSchema]:
        query = (
            insert(self.table)
            .values(PersonSchemaInsert.model_dump_many(data_list))
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
        order_by: list[str] | None = None,
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
        select_stmt = select_stmt.filter_by(**filter_by)
        return select_stmt

    def __enrich_select_order_by(
        self,
        select_stmt: Select[tuple[PersonTable]],
        order_by: list[str] | None,
    ) -> Select[tuple[PersonTable]]:
        if order_by is None:
            return select_stmt

        for column_name in order_by:
            is_desc = False
            if column_name.startswith('-'):
                is_desc = True
                column_name = column_name[1:]

            column: InstrumentedAttribute[Any] | None = getattr(
                PersonTable, column_name, None
            )
            if column is None:
                msg = f'Table {PersonTable.__tablename__} hasn`t column {column_name}'  # noqa:E501
                raise RepositoryErrorUnexistentColumn(msg)

            if is_desc is True:
                select_stmt = select_stmt.order_by(column.desc())
            else:
                select_stmt = select_stmt.order_by(column.asc())

        return select_stmt


class PersonRepositories:
    sqlalchemy_main = PersonRepository(
        sessionmaker=DatabaseConfig.main_config.sessionmaker,
    )
    sqlalchemy_test = PersonRepository(
        sessionmaker=DatabaseConfig.test_config.sessionmaker,
    )
