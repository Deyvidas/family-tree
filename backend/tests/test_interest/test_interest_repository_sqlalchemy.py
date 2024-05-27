import pytest
from sqlalchemy import select

from src.database import DatabaseConfig
from src.database.tables import InterestTable
from src.interest.repository import RepositoryInterface
from src.interest.schema import Schema
from tests.test_interest.interest_factory import generate_interest
from tests.test_interest.interest_factory import generate_interests


sessionmaker = DatabaseConfig.test_config.sessionmaker


@pytest.mark.usefixtures('use_database')
def test_create(repository: RepositoryInterface):
    """
    Test that the repository create method works correctly
        - Create new interest in the database
        - Returns the instance that was created, as schema
    """
    new_data = generate_interest()

    # Create new interest using the repository
    created = repository.create(new_data)
    assert isinstance(created, Schema)
    assert created.id == new_data.id
    assert str(created.created_at) == str(new_data.created_at)
    assert str(created.updated_at) == str(new_data.updated_at)
    assert created.name == new_data.name
    assert created.description == new_data.description

    # Check if the repository has really created new interest in the database
    filter_by = new_data.model_dump(mode='json')
    stmt = select(InterestTable).filter_by(**filter_by)
    with sessionmaker() as session:
        received = session.scalar(stmt)
    assert Schema.model_validate(received) == created


@pytest.mark.usefixtures('use_database')
def test_bulk_create(repository: RepositoryInterface):
    """
    Test the repository method bulk_create works correctly
        - Create a list of interests in the database
        - Returns the list of instances that were created, as schema
    """
    new_data_list = generate_interests(20)

    # Insert a list of interests using repository
    created_list = repository.bulk_create(new_data_list)
    assert len(created_list) == len(new_data_list)

    for created in created_list:
        assert isinstance(created, Schema)

        new_data = list(
            filter(lambda data: data.id == created.id, new_data_list)
        )
        assert len(new_data) == 1
        new_data = new_data[0]

        assert created.id == new_data.id
        assert str(created.created_at) == str(new_data.created_at)
        assert str(created.updated_at) == str(new_data.updated_at)
        assert created.name == new_data.name
        assert created.description == new_data.description

        # Check the database
        filter_by = new_data.model_dump(mode='json')
        stmt = select(InterestTable).filter_by(**filter_by)
        with sessionmaker() as session:
            received = session.scalar(stmt)
        assert Schema.model_validate(received) == created
