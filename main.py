from fastapi import FastAPI
import uvicorn
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi import Request


app = FastAPI()


templates = Jinja2Templates(directory="templates")

@app.get("/")
def root():
    return {"msg": "Здарова!"}

@app.get("/page", response_class=HTMLResponse)
def page(request: Request):
   return templates.TemplateResponse("index.html", {"request": request, "greeting": "Здарова, ублюдки!"})

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000)