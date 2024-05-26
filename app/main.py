from fastapi import FastAPI

import routers

app = FastAPI()
DATABASE = 'newq.db'

# Include routers
app.include_router(router=routers.router)

@app.get('/')
async def hello_world():
    return { "message" : "hello_world" }

