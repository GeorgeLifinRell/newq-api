from fastapi import FastAPI
import uvicorn
import routers

app = FastAPI()
DATABASE = 'newq.db'

# Include routers
app.include_router(router=routers.router)

@app.get('/')
async def hello_world():
    return { "message" : "hello_world" }

if __name__ == '__main__':
    uvicorn.run(app=app, host='0.0.0.0', port=8000)