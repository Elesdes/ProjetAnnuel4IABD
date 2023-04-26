from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()
app.mount('/static', StaticFiles(directory='static'), name='static')

templates = Jinja2Templates(directory="templates")


@app.get("/")
def root():
    return {"message": "Hello World"}


@app.get('/test', response_class=HTMLResponse)
def test(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
