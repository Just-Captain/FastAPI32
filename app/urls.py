from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from sqlalchemy.orm import Session
from sqlalchemy import select
from database import engine
from models import TaskModel

task_template = APIRouter()
task_template.mount('/static', StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory='templates')

@task_template.get('/')
def get_task_template(request: Request):
    session = Session(engine)
    stmt = select(TaskModel)
    requst_db = session.execute(stmt)
    tasks:list = requst_db.scalars().all()
    context = {}
    context['tasks'] = tasks
    session.close()
    return templates.TemplateResponse(
        request=request,
        name='tasks.html',
        context=context,
    )