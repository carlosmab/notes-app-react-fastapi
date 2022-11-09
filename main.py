
from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def getRoutes():
    return ['/notes', "/notes/<pk>"]

