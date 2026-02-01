from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from starlette.middleware.sessions import SessionMiddleware
from app.routes import router

app = FastAPI()

app.add_middleware(
    SessionMiddleware,
    secret_key="valentines-secret-key",
    max_age=60 * 60 * 6
)

app.mount("/static", StaticFiles(directory="app/static"), name="static")
app.include_router(router)
