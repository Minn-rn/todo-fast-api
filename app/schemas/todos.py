from pydantic import BaseModel, ConfigDict

# Базовая схема (общие поля)
class STodoBase(BaseModel):
    title: str
    description: str | None = None

# Схема для СОЗДАНИЯ задачи (клиент присылает title и description)
class STodoAdd(STodoBase):
    pass

# Схема для ОТВЕТА клиенту (чтение из БД)
class STodo(STodoBase):
    id: int
    is_completed: bool = False

    # Позволяет Pydantic читать данные напрямую из ORM-объектов SQLAlchemy
    model_config = ConfigDict(from_attributes=True)

# TODO: создать тут же схему для обновления задач.