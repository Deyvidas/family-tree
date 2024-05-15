from fastapi import FastAPI

from src.api.config import APIConfig
from src.api.utils import generate_api_docs

from .person import router as person_router


api_v1 = FastAPI(
    root_path='/api/v1',
    version='1.0.0',
    title=f'{APIConfig.title} [V1]',
    description=APIConfig.description,
    docs_url=None,
    redoc_url=None,
)

api_v1.include_router(router=person_router, prefix='/person', tags=['Person'])
generate_api_docs(api_v1, docs_url='/', redoc_url='/redoc')
