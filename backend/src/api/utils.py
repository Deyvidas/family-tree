from fastapi import FastAPI
from fastapi.openapi.docs import get_redoc_html
from fastapi.openapi.docs import get_swagger_ui_html


def generate_api_docs(app: FastAPI, *, docs_url='/docs', redoc_url='/redoc'):

    @app.get(path=docs_url, include_in_schema=False)
    async def swagger_html():
        return get_swagger_ui_html(
            openapi_url=f'{app.root_path}/openapi.json',
            title=app.title,
            swagger_css_url='/api/static/swagger-ui.css',
            swagger_js_url='/api/static/swagger-ui-bundle.js',
            swagger_favicon_url='/api/static/favicon.ico',
        )

    @app.get(path=redoc_url, include_in_schema=False)
    async def redoc_html():
        return get_redoc_html(
            openapi_url=f'{app.root_path}/openapi.json',
            title=app.title,
            redoc_js_url='/api/static/redoc.standalone.js',
        )
