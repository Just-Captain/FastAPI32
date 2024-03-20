from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import json
from fastapi.responses import HTMLResponse
import uvicorn
from pydantic import BaseModel

app = FastAPI() # <- создаем экземпляр класса
app.mount('/static', StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory='templates')

URLS = [
    {"tasks_post" : "127.0.0.1:8000/tasks/"}
]

class DatabaseJson:
    def __init__(self, name_db) -> None:
        self.__name_db = name_db

    def name_db(self):
        return self.__name_db

    def read(self) -> dict:
        with open(self.__name_db, 'r', encoding='utf-8') as db:
            return json.load(db)
    
    def write(self, data) -> None:
        with open(self.__name_db, 'w', encoding='utf-8') as db:
            json.dump(data, db, ensure_ascii=False)

database = DatabaseJson('database.json')


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
    tasks = database.read()
    return templates.TemplateResponse(request=request, name='tasks.html', context=tasks)



if __name__ == '__main__':
    print('Starting server')
    uvicorn.run('main:app', port=8000, reload=True)
    print('Server stopped')

# ls - комадна показывающая в консоле папки и файлы
# cd app - что бы перейти в директорию app
# cd .. - что бы вернуться на один уровень назад
# uvicorn main:app --reload