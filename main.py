from urllib import request
from fastapi import FastAPI, Form, Request
from fastapi.responses import FileResponse
from pydantic import BaseModel
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()

@app.get("/")
async def root(request : Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/features")
async def say_hello(request : Request):
    return templates.TemplateResponse("features.html", {"request": request})

@app.get("/about")
async def about(request : Request):
    return templates.TemplateResponse("about.html", {"request": request})
@app.get("/pricing")
async def pricing(request : Request):
    return templates.TemplateResponse("pricing.html", {"request": request})


