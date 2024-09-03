from fastapi import FastAPI
from src.routers import auth_router, friend_router

app = FastAPI()

app.include_router(
    auth_router,
    prefix='/api',
    tags=['auth']
)
app.include_router(
    friend_router,
    prefix='/api',
    tags=['friends']
)
