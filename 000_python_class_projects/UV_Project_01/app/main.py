from fastapi import FastAPI

app = FastAPI(
    title="Todo API",
    description="A learning Project for FastAPI",
    version="1.0.0"
)

app.include_router(todo_router, prefix="/api")
