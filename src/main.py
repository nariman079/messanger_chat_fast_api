from fastapi import FastAPI
from src.routers import auth_router

app = FastAPI()

app.include_router(
    auth_router,
    prefix='/api',
    tags=['auth']
)
