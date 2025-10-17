from fastapi import FastAPI
from fastapi.responses import FileResponse

app = FastAPI()

@app.get("/")
async def root():
    return FileResponse("index.html")

@app.get("/features")
async def features():
    return FileResponse("features.html")

@app.get("/about")
async def about():
    return FileResponse("about.html")

@app.get("/pricing")
async def pricing():
    return FileResponse("pricing.html")

