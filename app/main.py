from fastapi import FastAPI
from app.db.model import Answer

from app.api import api

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Fast API in Python"}


@app.post("/summary")
def read_user(payload: Answer):
    payload = payload.dict()
    return api.aws_titan_summarisation(payload)

