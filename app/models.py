from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Boolean
from database import Model


class TaskModel(Model):
    __tablename__ = "task_table"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] 
    description: Mapped[str] 
    status: Mapped[bool] = mapped_column(Boolean, default=False)

