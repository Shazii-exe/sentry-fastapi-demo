import os

import sentry_sdk
from fastapi import FastAPI
from dotenv import load_dotenv

load_dotenv()

sentry_sdk.init(
    dsn=os.getenv("dsn"),
    environment="development",
)

app = FastAPI()


@app.get("/")
def home():
    return {"message": "FastAPI is running!"}


@app.get("/error")
def trigger_error():
    result = 10 / 0
    return {"result": result}