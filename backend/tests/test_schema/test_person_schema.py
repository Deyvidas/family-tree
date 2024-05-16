from src.person.schema.person_schema import PersonSchema
from src.person.schema.person_schema import PersonSchemaFULL
from src.person.schema.person_schema import PersonSchemaPOST


class Test:
    def test_base_schema(self):
        must_have_fields = {
            'name',
            'surname',
            'patronymic',
            'gender',
            'birth_date',
        }

        assert set(PersonSchema.model_fields.keys()) == must_have_fields

    def test_FULL_schema(self):
        must_have_fields = {
            'id',
            'created_at',
            'updated_at',
            'name',
            'surname',
            'patronymic',
            'gender',
            'birth_date',
        }

        assert set(PersonSchemaFULL.model_fields.keys()) == must_have_fields

    def test_POST_schema(self):
        must_have_fields = {
            'name',
            'surname',
            'patronymic',
            'gender',
            'birth_date',
        }

        assert set(PersonSchemaPOST.model_fields.keys()) == must_have_fields
