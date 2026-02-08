from fastapi import FastAPI
from app.api.todos import router as todo_router

app = FastAPI(
    title="Todo API",
    description="A learning Project for FastAPI",
    version="1.0.0"
)

app.include_router(todo_router, prefix="/api")

# app.include_router(user_router, prefix="/user")