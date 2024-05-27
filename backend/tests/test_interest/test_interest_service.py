from datetime import datetime

import pytest

from src.common.schema import TZ_UTC
from src.interest.schema import SchemaGET
from src.interest.schema import SchemaPOST
from src.interest.service import Service
from tests.test_interest.interest_factory import generate_interest


@pytest.mark.usefixtures('use_database', 'freezer')
def test_create(service: Service):
    """
    Test that the service create method works correctly:
        - All fields that were not passed, such as id, created_at, and
          updated_at, have been initialized
        - After creation, the data is returned as a GET schema
    """
    datetime_now = datetime.now(TZ_UTC)
    data = generate_interest()
    new_data = SchemaPOST(
        name=data.name,
        description=data.description,
    )

    created = service.create(new_data)
    assert isinstance(created, SchemaGET)
    assert created.id is not None
    assert str(created.created_at) == str(datetime_now)
    assert str(created.updated_at) == str(datetime_now)
    assert created.name == new_data.name
    assert created.description == new_data.description
