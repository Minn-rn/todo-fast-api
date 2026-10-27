from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase, MappedAsDataclass

from typing import Annotated
from fastapi import Depends

DATABASE_URL = "sqlite+aiosqlite:///todo.db"

engine = create_async_engine(DATABASE_URL)  # Главный мост с базой данных

new_session = async_sessionmaker(engine, expire_on_commit=False) # Создание сессий

# Базовый класс для моделей БД
# MappedAsDataclass - нужен для удобной работы с типами.
class Model(MappedAsDataclass, DeclarativeBase):
    pass

# Наша зависимость (Ассистент)
async def get_db():
    async with new_session() as session:
        yield session

# Создаем аннотацию типов
SessionDep = Annotated[AsyncSession, Depends(get_db)]

# автоматически создает и закрывает подключение к базе
