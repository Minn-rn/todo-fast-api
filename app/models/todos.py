from sqlalchemy.orm import Mapped, mapped_column
from app.database import Model

class TodoModel(Model):
    __tablename__ = 'todos'

    id: Mapped[int] = mapped_column(primary_key=True, init=False)
    title: Mapped[str]
    description: Mapped[str | None] = None
    is_completed: Mapped[bool] = False

    is_deleted: Mapped[bool] = False