from src.person.schema.person_filter import PersonFilter
from src.person.schema.person_filter import PersonFilterFULL


class Test:
    def test_base_filter(self):
        can_filter_by = {
            'name',
            'surname',
            'patronymic',
            'gender',
            'birth_date',
        }

        assert set(PersonFilter.model_fields.keys()) == can_filter_by

    def test_FULL_filter(self):
        can_filter_by = {
            'id',
            'created_at',
            'updated_at',
            'name',
            'surname',
            'patronymic',
            'gender',
            'birth_date',
        }

        assert set(PersonFilterFULL.model_fields.keys()) == can_filter_by
