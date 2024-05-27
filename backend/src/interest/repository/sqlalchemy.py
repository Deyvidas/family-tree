from typing import Any

from sqlalchemy import Select
from sqlalchemy import insert
from sqlalchemy import select
from sqlalchemy.orm import InstrumentedAttribute

from src.common.types import OrderBy
from src.database import DatabaseConfig
from src.database.tables import InterestTable

from ..schema import Schema
from .interface import RepositoryInterface


class RepositorySqlalchemy(RepositoryInterface):
    _table = InterestTable
    _schema = Schema
    _sessionmaker = DatabaseConfig.main_config.sessionmaker

    def create(
        self,
        data: Schema,
    ) -> Schema:
        stmt = (
            insert(self._table)
            .values(**data.model_dump(mode='json'))
            .returning(self._table)
        )

        with self._sessionmaker() as session:
            new_interest_row = session.scalars(stmt).one()
            session.commit()
            return self._schema.model_validate(new_interest_row)

    def bulk_create(
        self,
        data_list: list[Schema],
    ) -> list[Schema]:
        stmt = (
            insert(self._table)
            .values(self._schema.many().dump_python(data_list, mode='json'))
            .returning(self._table)
        )

        with self._sessionmaker() as session:
            new_interests_rows = list(session.scalars(stmt).all())
            session.commit()
            return self._schema.many().validate_python(new_interests_rows)

    def filter(
        self,
        filter_by: dict[str, Any] | None = None,
        order_by: list[OrderBy] | None = None,
    ) -> list[Schema]:
        stmt = select(self._table)
        stmt = self._enrich_select_with_filter_by(stmt, filter_by)
        stmt = self._enrich_select_with_order_by(stmt, order_by)

        with self._sessionmaker() as session:
            interests_list = list(session.scalars(stmt).all())
            return self._schema.many().validate_python(interests_list)

    def _enrich_select_with_filter_by(
        self,
        select: Select[tuple[InterestTable]],
        filter_by: dict[str, Any] | None,
    ) -> Select[tuple[InterestTable]]:
        if filter_by is None:
            return select
        return select.filter_by(**filter_by)

    def _enrich_select_with_order_by(
        self,
        select: Select[tuple[InterestTable]],
        order_by: list[OrderBy] | None,
    ) -> Select[tuple[InterestTable]]:
        if order_by is None:
            return select

        for order in order_by:
            field: InstrumentedAttribute[Any] = getattr(
                InterestTable, order.field
            )
            match order.direction:
                case 'asc':
                    select = select.order_by(field.asc())
                case 'desc':
                    select = select.order_by(field.desc())

        return select
