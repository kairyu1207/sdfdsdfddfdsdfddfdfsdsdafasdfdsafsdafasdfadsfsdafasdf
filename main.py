from fastapi import FastAPI
from fastapi.responses import FileResponse

app = FastAPI()

@app.get("/")
async def root():
    return FileResponse("templates/index.html")

@app.get("/features")
async def features():
    return FileResponse("templates/features.html")

@app.get("/about")
async def about():
    return FileResponse("templates/about.html")

@app.get("/pricing")
async def pricing():
    return FileResponse("templates/pricing.html")
