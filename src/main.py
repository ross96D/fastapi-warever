from fastapi import FastAPI

def _app() -> FastAPI:
    aplication = FastAPI()
    return aplication

app:FastAPI = _app()
