import pytest

from src.person.service.person_service import PersonServices


service = PersonServices.test_service


@pytest.mark.usefixtures('use_database')
class TestGetAll:
    def test_output_order(self):
        """"""
        assert False


@pytest.mark.usefixtures('use_database')
class TestGetStrictOne:
    def test_get_strict_one(self):
        """"""
        assert False


@pytest.mark.usefixtures('use_database')
class TestFilterBy:
    def test_filter_by(self):
        """"""
        assert False


@pytest.mark.usefixtures('use_database')
class TestCreatePerson:
    def test_create_person(self):
        """"""
        assert False
