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
    try:
        result = 10 / 0
    except ZeroDivisionError:
        sentry_sdk.capture_message("Division by zero attempted", level="warning")
        return {"error": "Division by zero is not allowed"}
    return {"result": result}