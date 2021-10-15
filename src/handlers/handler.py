from fastapi import FastAPI
from mangum import Mangum

app = FastAPI()


@app.get("/test")
def pong():
    return {"Ping": "pong"}


api = Mangum(app)
