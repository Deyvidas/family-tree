import pytest
from fastapi.testclient import TestClient

from src.api import app


@pytest.fixture
def client() -> TestClient:
    return TestClient(
        app=app,
        base_url='http://testserver/api/v1',
    )
