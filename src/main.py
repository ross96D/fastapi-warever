from fastapi import FastAPI
from src.routes import router


def _app() -> FastAPI:
    aplication = FastAPI()
    aplication.include_router(router)
    return aplication


app: FastAPI = _app()
