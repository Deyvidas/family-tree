import pytest
from sqlalchemy import insert

from src.database import DatabaseConfig
from src.database.tables import InterestTable
from src.interest.repository import RepositorySqlalchemy
from src.interest.schema import Schema
from src.interest.service import Service
from tests.test_interest.interest_factory import generate_interests


sessionmaker = DatabaseConfig.test_config.sessionmaker


class InterestRepositorySqlalchemyTest(RepositorySqlalchemy):
    _sessionmaker = sessionmaker


@pytest.fixture
def repository() -> InterestRepositorySqlalchemyTest:
    return InterestRepositorySqlalchemyTest()


@pytest.fixture
def service(repository: InterestRepositorySqlalchemyTest) -> Service:
    return Service(repository)


@pytest.fixture
def populate_database() -> list[Schema]:
    values = Schema.many().dump_python(
        generate_interests(20),
        mode='json',
    )
    stmt = insert(InterestTable).values(values).returning(InterestTable)
    with sessionmaker() as session:
        new_interests = list(session.scalars(stmt).all())
        session.commit()
        return Schema.many().validate_python(new_interests)
