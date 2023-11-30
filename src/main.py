from fastapi import FastAPI
from src.routes.artist import router as artist_router
from src.routes.album import router as album_router


def _app() -> FastAPI:
    aplication = FastAPI()
    aplication.include_router(artist_router)
    aplication.include_router(album_router)
    return aplication


app: FastAPI = _app()
