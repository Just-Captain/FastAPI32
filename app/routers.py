from fastapi import APIRouter, Request
from sqlalchemy.orm import Session
from database import engine
from sqlalchemy import select
from models import TaskModel


tasks_router = APIRouter(prefix="/api/v1/tasks")

"""
    file = open('data.txt')
    file.write()
"""

@tasks_router.get(path='/list/') # <- декоратор который указывает что функция определенная ниже будет обрабатывать запросы по такому пути как /list/, полный путь такой /api/v1/tasks/list/
def list_task_point(request: Request): # <- Функция которая принимает параметр request типа Request, который содержит в себе информацию о запросе клиента.
    session = Session(engine) # <- создаёт экземпляр класса сесси для работы с базой данных. Используетяс для подключение к БД
    stmt = select(TaskModel) # <- формирует SQL запрос для выборки всех записей из таблицы сопоставленной с моделью TaskModel
    """
    SELECT task.id, task.title, task.description, task.done 
    FROM task <- ссырой SQL запрос
    """
    requst_db = session.execute(stmt) # <- Запрос выполняется с помощью созданной сессии, в результате мы получаем обьект, который соджерит результат запроса
    tasks:list = requst_db.scalars().all() #<- Полученный обьект с результатом преобразуем в список значений при помощи метода scalars() и из него извелаються все значения с помощью метода all()
    session.close() # <- Сеесия закрывается для осовобождения ресурсов связанных с БД.
    if len(tasks) == 0:
        return {"message": "У вас нет задач"}
    else:
        return {"message": tasks} # <- возвращает словарь, который преобразуется в JSON, который будет возвращен клиенту в ответ на запрос.

    