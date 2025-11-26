import uvicorn
from fastapi import FastAPI
from routes import csv_route
app = FastAPI()

@app.get("base")
def welcome():
    return {"massage":"welcome the base שבעת הכוכבים"}

app.include_router(csv_route.router)



if __name__ == '__main__':
    uvicorn.run("main:app",host="127.0.0.1",port=8000,reload=True)