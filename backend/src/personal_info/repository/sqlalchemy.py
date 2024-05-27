from sqlalchemy import insert

from src.database import DatabaseConfig
from src.database.tables import PersonalInfoTable

from ..schema import Schema
from .interface import RepositoryInterface


class RepositorySqlalchemy(RepositoryInterface):
    _table = PersonalInfoTable
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
            new_entity = session.scalars(stmt).one()
            session.commit()
            return self._schema.model_validate(new_entity)
