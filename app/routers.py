from fastapi import APIRouter, Request
from sqlalchemy.orm import Session
from database import engine
from sqlalchemy import select, insert, update, delete
from models import TaskModel
from schemas import TaskCreateSchema, TaskUpdateSchema

tasks_router = APIRouter(prefix="/api/v1/tasks")

"""
    file = open('data.txt')
    file.write()
"""

@tasks_router.get(path='/list/') # <- декоратор который указывает что функция определенная ниже будет обрабатывать запросы по такому пути как /list/, полный путь такой /api/v1/tasks/list/
def list_task_point(request: Request): # <- Функция которая принимает параметр request типа Request, который содержит в себе информацию о запросе клиента.
    session:Session = Session(engine) # <- создаёт экземпляр класса сесси для работы с базой данных. Используетяс для подключение к БД
    stmt = select(TaskModel) # <- формирует SQL запрос для выборки всех записей из таблицы сопоставленной с моделью TaskModel
    """
    SELECT task.id, task.title, task.description, task.done 
    FROM task <- ссырой SQL запрос
    """
    requst_db = session.execute(stmt) # <- Запрос выполняется с помощью созданной сессии, в результате мы получаем обьект, который соджерит результат запроса
    tasks:list = requst_db.scalars().all() #<- Полученный обьект с результатом преобразуем в список значений при помощи метода scalars() и из него извелаються все значения с помощью метода all()
    session.close() # <- Сеесия закрывается для осовобождения ресурсов связанных с БД.
    return tasks

@tasks_router.post(path='/create/')
def create_task_point(request: Request, task: TaskCreateSchema):
    session = Session(engine)
    stmt = insert(TaskModel).values(title=task.title,
                                    description=task.description)
    session.execute(stmt)
    session.commit()
    session.close()
    return task

@tasks_router.put(path='/update/')
def update_task_point(request: Request, task_id:int ,new_task: TaskUpdateSchema):
    session = Session(engine)
    stmt = update(TaskModel).where(TaskModel.id == task_id).values(
        title=new_task.title,
        description=new_task.description,
        status=new_task.status
    )
    task = session.execute(stmt)
    session.commit()
    session.close()
    return new_task

# URL Ваш вариант - 'http://127.0.0.1:8000/api/v1/tasks/delete/5/' @tasks_router.delete(path='/delete/{task_id}/')
# URL  мой вариант - 'http://127.0.0.1:8000/api/v1/tasks/delete/?task_id=5'
@tasks_router.delete(path='/delete/')
def delete_task_point(request: Request, task_id: int):
    session = Session(engine)
    stmt = delete(TaskModel).where(TaskModel.id == task_id)
    result = session.execute(stmt)
    session.commit()
    session.close()
    return result