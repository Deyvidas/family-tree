from src.person.schema.person_fields import PersonFields
from src.person.schema.person_schema import PersonSchema


class PersonSchemaGET(PersonSchema):
    pass


class PersonSchemaPOST(PersonSchema):
    id: PersonFields.id = PersonFields.exclude
    created_at: PersonFields.created_at = PersonFields.exclude
    updated_at: PersonFields.updated_at = PersonFields.exclude
