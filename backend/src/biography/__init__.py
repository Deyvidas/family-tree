from . import repository
from .schema import Schema as Schema
from .schema import SchemaGET as SchemaGET
from .schema import SchemaGETRef as SchemaGETRef
from .schema import SchemaPOST as SchemaPOST
from .schema import SchemaPOSTRef as SchemaPOSTRef
from .service import Service as Service


service = Service(repository.RepositorySqlalchemy())
