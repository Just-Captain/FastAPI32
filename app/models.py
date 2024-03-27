from database import Model
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Boolean


class TaskModel(Model):
    __tablename__ = "task"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] 
    description: Mapped[str] 
    done: Mapped[bool] = mapped_column(Boolean, default=False)

