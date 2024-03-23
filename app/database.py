from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

engine = create_engine("sqlite:///db.sqlite", echo=True)



class Model(DeclarativeBase):
    pass

class Task(Model):
    __tablename__ = "task"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] 
    description: Mapped[str] 
    done: Mapped[bool]

