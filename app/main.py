from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import json
from fastapi.responses import HTMLResponse

from pydantic import BaseModel

app = FastAPI() # <- создаем экземпляр класса
app.mount('/static', StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory='templates')

URLS = [
    {"tasks_post" : "127.0.0.1:8000/tasks/"}
]

def database(name_db, mode, data=None):
    if mode == 'r':
        with open(name_db, mode, encoding='utf-8') as db:
            return json.load(db)
    elif mode == 'w':
        with open(name_db, mode, encoding='utf-8') as db:
            json.dump(data, db)


class Task(BaseModel):
    """
    Схема обьекта, которую мы ожидаем получить от клиента
    """
    title:str
    description:str

@app.post('/tasks/')
def create_task(request:Request, task:Task):
    task = {"title": task.title,"description": task.description}
    tasks = database('database.json', 'r')
    tasks['tasks'].append(task)
    database('database.json', 'w', tasks)


@app.get('/tasks/')
def get_tasks(request:Request):
    tasks = database('database.json', 'r')
    tasks['url'] = 'http://127.0.0.1:8000/tasks/'
    return templates.TemplateResponse(request=request, name='tasks.html', context=tasks)

# ls - комадна показывающая в консоле папки и файлы
# cd app - что бы перейти в директорию app
# cd .. - что бы вернуться на один уровень назад
# uvicorn main:app --reload