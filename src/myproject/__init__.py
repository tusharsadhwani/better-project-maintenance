"""API endpoints for app."""
import uuid

from fastapi import FastAPI

from myproject.models.user import UserModel
from myproject.models.message import Message


app = FastAPI()


@app.get("/")
def home():
    return "This is the home page"


@app.get("/api")
def api_root():
    return {"message": "Hello world!"}


@app.get("/api/v1/user")
def get_user() -> UserModel:
    return UserModel(userid=uuid.uuid4(), username="Michael")


@app.get("/api/v1/messages")
def get_messages() -> list[Message]:
    return [
        Message(message_id=uuid.uuid4(), text="Hello"),
        Message(message_id=uuid.uuid4(), text="Test"),
    ]
