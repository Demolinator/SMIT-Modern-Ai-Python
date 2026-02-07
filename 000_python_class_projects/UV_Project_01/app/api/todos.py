from fastapi import APIRouter, HTTPException, status


router = APIRouter(tags=["Todos"])


@router.post("/todos")
def create_todo():
    