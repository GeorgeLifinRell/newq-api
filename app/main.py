from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import sqlite3

app = FastAPI()
DATABASE = 'newq.db'

@app.get('/')
async def hello_world():
    return { "message" : "hello_world" }

