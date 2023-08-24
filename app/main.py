from fastapi import FastAPI
from app.db.model import Answer
from fastapi.middleware.cors import CORSMiddleware
from app.api import api

app = FastAPI()

# Allow all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "OPTIONS", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "Fast API in Python"}


@app.post("/summary")
def read_user(payload: Answer):
    payload = payload.dict()
    return api.aws_titan_summarisation(payload)

