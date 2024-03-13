from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import json
from fastapi.responses import HTMLResponse

from pydantic import BaseModel

app = FastAPI() # <- создаем экземпляр класса
app.mount('/static', StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory='templates')


def database(name_db, mode, data=None):
    if mode == 'r':
        with open(name_db, mode, encoding='utf-8') as db:
            return json.load(db)
    elif mode == 'w':
        with open(name_db, mode, encoding='utf-8') as db:
            json.dump(data, db)

@app.get('/test/', response_class=HTMLResponse)
def test(request:Request):
    html_content = """
    <html>
        <body>
            <h1>Hello</h1>
        </body>
    </html>
 
"""
    return HTMLResponse(content=html_content, status_code=200)

class Task(BaseModel):
    title:str
    description:str

@app.post('/task_list/')
def create_task(request:Request, task:Task):
    print(task)
    tasks = database('database.json', 'r')
    return templates.TemplateResponse(request=request, name='task_list.html', context=tasks)

@app.get('/task_list/')
def list_task(request:Request):
    tasks = database('database.json', 'r')
    return templates.TemplateResponse(request=request, name='task_list.html', context=tasks)

@app.get('/users/')
def users(request:Request):
    users = database('database.json', 'r')
    return templates.TemplateResponse(request=request, name='users.html', context=users)
# ls - комадна показывающая в консоле папки и файлы
# cd app - что бы перейти в директорию app
# cd .. - что бы вернуться на один уровень назад
# uvicorn main:app --reload