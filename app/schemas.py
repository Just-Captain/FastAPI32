from pydantic import BaseModel


class TaskCreateSchemas(BaseModel):
    title: str
    description: str

