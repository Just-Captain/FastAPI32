from pydantic import BaseModel


class TaskCreateSchema(BaseModel):
    title: str
    description: str

class TaskUpdateSchema(TaskCreateSchema):
    status: bool