from fastapi import APIRouter, Depends

from sqlalchemy import select

from app.database import SessionDep
from app.models.todos import TodoModel
from app.schemas.todos import STodoAdd, STodo

router = APIRouter(prefix="/todos", tags=["Задачи"])

@router.post("", response_model=STodo)
async def create_todo(
        todo: STodoAdd,
        session: SessionDep
):
    new_todo = TodoModel(**todo.model_dump())

    session.add(new_todo)
    await session.commit()
    await session.refresh(new_todo)

    return new_todo

@router.get("", response_model=list[STodo])
async def get_todos(session: SessionDep):
    query = select(TodoModel)

    result = await session.execute(query)

    return result.scalars().all()

# TODO: реализовать полный CRUD проект (put, patch, delete, get(id))