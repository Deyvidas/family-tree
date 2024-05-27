from fastapi import FastAPI

from src.api.config import APIConfig
from src.api.utils import generate_api_docs

from .interest import router as interest_router
from .person import router as person_router
from .personal_info import router as personal_info_router


api_v1 = FastAPI(
    root_path='/api/v1',
    version='1.0.0',
    title=f'{APIConfig.title} [V1]',
    description=APIConfig.description,
    docs_url=None,
    redoc_url=None,
)

api_v1.include_router(
    router=interest_router,
    prefix='/interests',
    tags=['Interests'],
)
api_v1.include_router(
    router=person_router,
    prefix='/people',
    tags=['People'],
)
api_v1.include_router(
    router=personal_info_router,
    prefix='/personal-info',
    tags=['Personal information'],
)

generate_api_docs(api_v1, docs_url='/', redoc_url='/redoc')
