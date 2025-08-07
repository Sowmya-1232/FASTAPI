from fastapi import FastAPI
from pydantic import BaseModel
from model import model
import uvicorn

app = FastAPI()
class InputData(BaseModel):
    feature1: float

@app.get('/') 
def index():
    return {'message':'hello world'}