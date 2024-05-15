from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from .config import APIConfig
from .utils import generate_api_docs
from .v1 import api_v1


app = FastAPI(
    root_path='/api',
    version='0.0.0',
    title=APIConfig.title,
    description=APIConfig.description,
    docs_url=None,
    redoc_url=None,
)

app.mount('/static', StaticFiles(directory='static/api_doc'), name='static')
app.mount('/v1', api_v1, name='v1')
generate_api_docs(app, docs_url='/', redoc_url='/redoc')
