import uvicorn
from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi
from app.routers import converter

app = FastAPI(title='Currency Converter',
              docs_url=None)

def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Currency convertor API",
        version="1.0.0",
        description="Конвертер валют",
        routes=app.routes,
    )
    app.openapi_schema = openapi_schema
    return app.openapi_schema
app.openapi = custom_openapi

app.include_router(converter.router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)


