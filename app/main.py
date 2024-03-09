from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles


app = FastAPI() # <- создаем экземпляр класса
app.mount('/static', StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory='templates')


@app.get('/') # <- декоратор, который обрабатывает get запросы по маршруту 127.0.0.1:8000/
def index(request:Request):
    return templates.TemplateResponse(request=request, name='index.html')

@app.get('/about/') # <- 127.0.0.1:8000/about/
def about(request:Request):
    return templates.TemplateResponse(request=request, name='about.html')

"""
@app.get('/about/') # <- 127.0.0.1:8000/about/
def about(request:Request):
    return {"first_name": "Yury", "last_name": "Antsiferov"}
    """

# ls - комадна показывающая в консоле папки и файлы
# cd app - что бы перейти в директорию app
# cd .. - что бы вернуться на один уровень назад
# uvicorn main:app --reload