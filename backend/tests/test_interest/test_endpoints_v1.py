import pytest
from fastapi import FastAPI
from fastapi import status
from fastapi.testclient import TestClient

from src.api.v1 import api_v1
from src.api.v1.interest import get_interest_service
from src.interest.schema import SchemaGET
from src.interest.schema import SchemaPOST
from src.interest.service import Service
from tests.test_interest.conftest import InterestRepositorySqlalchemyTest
from tests.test_interest.interest_factory import generate_interest


@pytest.fixture
def get_app(repository: InterestRepositorySqlalchemyTest) -> FastAPI:
    app = api_v1

    def get_test_service():
        return Service(repository)

    app.dependency_overrides[get_interest_service] = get_test_service
    return app


@pytest.fixture
def client(get_app: FastAPI) -> TestClient:
    return TestClient(
        app=get_app,
        base_url='http://testserver/api/v1/interests',
    )


@pytest.mark.usefixtures('use_database', 'freezer')
def test_create_one_interest(client: TestClient):
    """
    Test that endpoint is working correctly
        - Response with status code 201
        - Return the correct data structure
    """
    data = generate_interest()
    post_data = SchemaPOST(
        name=data.name,
        description=data.description,
    )

    response = client.post(
        url='/',
        json=post_data.model_dump(mode='json'),
    )
    assert response.status_code == status.HTTP_201_CREATED
    response_model = SchemaGET.model_validate_json(response.content)
    assert response_model.name == post_data.name
    assert response_model.description == post_data.description
