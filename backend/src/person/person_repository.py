from src.common.repository import BaseRepository
from src.database import DatabaseConfig
from src.database.tables import PersonTable

from .schema.person_filter import PersonFilterFULL
from .schema.person_schema import PersonSchemaFULL
from .schema.person_schema import PersonSchemaPOST


class PersonRepository:
    sql_alchemy = BaseRepository(
        table=PersonTable,
        sessionmaker=DatabaseConfig.main_config.sessionmaker,
        schema_full=PersonSchemaFULL,
        schema_insert=PersonSchemaPOST,
        filter_schema=PersonFilterFULL,
    )

    sql_alchemy_test = BaseRepository(
        table=PersonTable,
        sessionmaker=DatabaseConfig.test_config.sessionmaker,
        schema_full=PersonSchemaFULL,
        schema_insert=PersonSchemaPOST,
        filter_schema=PersonFilterFULL,
    )
