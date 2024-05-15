from datetime import datetime
from time import sleep

import pytest
from sqlalchemy.engine.base import Engine
from sqlalchemy.orm.session import Session
from sqlalchemy_utils import create_database
from sqlalchemy_utils import database_exists
from sqlalchemy_utils import drop_database

from src.database import DatabaseConfig
from src.database.tables import BaseTable


def pytest_sessionstart(session):
    """Before than test session is started create DB."""
    create_db(DatabaseConfig.test_config.engine)
    message = f' Tests are started at: {datetime.now()} '
    print('\n{:*^79}\n'.format(message))


def pytest_sessionfinish(session, exitstatus):
    """Drop database when test session is ended."""
    message = f' Tests are finished at: {datetime.now()} '
    print('\n\n{:*^79}\n'.format(message))
    drop_db(DatabaseConfig.test_config.engine)


@pytest.fixture(scope='session')
def session():
    """Initialize context of sqlalchemy.orm.Session."""
    with DatabaseConfig.test_config.sessionmaker() as session:
        yield session


# @pytest.fixture(scope='session', autouse=True)
# def switch_used_session_in_dependencies(session: Session) -> None:
#     """Switch used session into endpoints depends."""

#     def test_session():
#         yield session

#     banking_app.dependency_overrides[activate_session] = test_session


@pytest.fixture
def use_database(session: Session):
    engine = DatabaseConfig.test_config.engine

    try:
        engine.echo = False
        create_tables(engine, session)
        engine.echo = DatabaseConfig.test_config.engine_config.echo
        yield
        engine.echo = False
        drop_tables(engine, session)
        engine.echo = DatabaseConfig.test_config.engine_config.echo
    except Exception:
        pass
    finally:
        engine.echo = DatabaseConfig.test_config.engine_config.echo


def create_db(engine: Engine) -> None:
    """Execute command in command line which create DB."""

    drop_db(engine)
    sleep(1)  # Sleep is required!
    create_database(engine.url)
    engine.logger.info(f'|| DB CREATED SUCCESSFULLY (url={engine.url}) ||')


def drop_db(engine: Engine) -> None:
    """Execute command in command line which drop DB."""

    if not database_exists(engine.url):
        return

    drop_database(engine.url)
    engine.logger.info(f'|| DB DROPPED SUCCESSFULLY (url={engine.url}) ||')


def create_tables(engine: Engine, session: Session) -> None:
    """Create all registered into BaseTable.metadata tables."""

    drop_tables(engine, session)
    BaseTable.metadata.create_all(engine)
    session.commit()

    message = '\n{:*^79}'.format(' BaseTable.metadata.create_all() OK! ')
    engine.logger.info(message)


def drop_tables(engine: Engine, session: Session) -> None:
    """Drop all registered into BaseTable.metadata tables."""

    session.rollback()
    BaseTable.metadata.drop_all(engine)
    session.commit()

    message = '\n{:*^79}'.format(' BaseTable.metadata.drop_all() OK! ')
    engine.logger.info(message)
