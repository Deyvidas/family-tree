from fastapi import FastAPI

from src.api.v1.person import router as person_router


PREFIX = '/api/v1'

app = FastAPI()
app.include_router(router=person_router, prefix=PREFIX)
