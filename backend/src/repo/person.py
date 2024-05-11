from sqlalchemy import insert
from sqlalchemy import select

from src.database.config import config
from src.tables.person import PersonTable


class PersonRepo:
    session = config.session
    table = PersonTable

    def get_all(self):
        stmt = select(self.table)

        with self.session() as session:
            return session.scalars(stmt).all()

    def create_user(self, **kwargs):
        stmt = insert(self.table).values(**kwargs).returning(self.table)

        with self.session() as session:
            instance = session.scalars(stmt).one()
            session.commit()
            return instance
