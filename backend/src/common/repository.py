from dataclasses import dataclass

from sqlalchemy import Select
from sqlalchemy import insert
from sqlalchemy import select
from sqlalchemy.orm import InstrumentedAttribute
from sqlalchemy.orm import Session
from sqlalchemy.orm import sessionmaker as sqlalchemy_sessionmaker

from src.database.tables.base_table import BaseTable

from .exceptions import RepositoryErrorUnexistentColumn
from .schema.filter import BaseModelForFilter
from .schema.schema import BaseModelForSchema


@dataclass
class BaseRepository[
    TTable: BaseTable,
    TSchemaFull: BaseModelForSchema,
    TSchemaInsert: BaseModelForSchema,
    TFilter: BaseModelForFilter,
]:
    table: type[TTable]
    sessionmaker: sqlalchemy_sessionmaker[Session]

    schema_full: type[TSchemaFull]
    schema_insert: type[TSchemaInsert]
    filter_schema: type[TFilter]

    def create(
        self,
        data: TSchemaInsert,
    ) -> TSchemaFull:
        stmt = (
            insert(self.table)
            .values(**data.model_dump())
            .returning(self.table)
        )
        with self.sessionmaker() as session:
            instance = session.scalars(stmt).one()
            session.commit()
            return self.schema_full.model_validate(instance)

    def bulk_create(
        self,
        data_list: list[TSchemaInsert],
    ) -> list[TSchemaFull]:
        kwargs_list = [kw.model_dump() for kw in data_list]
        stmt = insert(self.table).values(kwargs_list).returning(self.table)
        with self.sessionmaker() as session:
            instances = list(session.scalars(stmt).all())
            session.commit()
            return self.schema_full.model_validate_many(instances)

    def filter(
        self,
        filter_by: TFilter | None = None,
        order_by: list[str] | None = None,
    ) -> list[TSchemaFull]:
        """
        Example of usage:
        ```py
        .filter(
            filter_by={'age': '43', ...},
            order_by=['gender', '-created_at', ...],
        )
        ```
        The sign before the column name means that the order of sorting must be
        descending. If this sign is not provided, it means that the sorting
        must be ascending.

        The SQL output:
        ```sql
          SELECT [...columns]
            FROM [table]
        ORDER BY gender ASC,
                 created_at DESC;
        ```
        """
        stmt = select(self.table)

        if filter_by is not None:
            stmt = self._enrich_select_with_filter_by(stmt, filter_by)
        if order_by is not None:
            stmt = self._enrich_select_with_order_by(stmt, order_by)

        with self.sessionmaker() as session:
            instances = list(session.scalars(stmt).all())
            return self.schema_full.model_validate_many(instances)

    def _enrich_select_with_filter_by(
        self,
        stmt: Select,
        filter: TFilter,
    ) -> Select:
        stmt = stmt.filter_by(**filter.model_dump(exclude_unset=True))
        return stmt

    def _enrich_select_with_order_by(
        self,
        stmt: Select,
        columns: list[str],
    ) -> Select:
        for column_name in columns:
            is_desc = False
            if column_name.startswith('-'):
                is_desc = True
                column_name = column_name[1:]

            column: InstrumentedAttribute | None = getattr(
                self.table, column_name, None
            )
            if column is None:
                msg = f'Cannot order by `{column_name}` because the `{self.table.__tablename__}` table does not have this column'  # fmt:skip # noqa:E501
                raise RepositoryErrorUnexistentColumn(msg)

            if is_desc:
                stmt = stmt.order_by(column.desc())
            else:
                stmt = stmt.order_by(column.asc())
        return stmt
