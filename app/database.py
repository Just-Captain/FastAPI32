from sqlalchemy import create_engine, Boolean
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

engine = create_engine("sqlite:///db.sqlite", echo=True)



class Model(DeclarativeBase):
    pass

class TaskModel(Model):
    __tablename__ = "task"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] 
    description: Mapped[str] 
    done: Mapped[bool] = mapped_column(Boolean, default=False)

