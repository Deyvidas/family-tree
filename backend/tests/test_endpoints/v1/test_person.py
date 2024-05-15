import pytest
from fastapi import status
from fastapi.testclient import TestClient


@pytest.mark.usefixtures('use_database')
class Test:

    def test_get_all_people(self, client: TestClient):
        resp = client.get('/person')
        assert resp.status_code == status.HTTP_200_OK
