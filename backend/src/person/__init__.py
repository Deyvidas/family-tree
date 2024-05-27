from . import repository
from .schema import Schema as Schema
from .schema import SchemaGET as SchemaGET
from .schema import SchemaPOST as SchemaPOST
from .service import Service as Service


service = Service(repository.RepositorySqlalchemy())
