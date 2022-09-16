from pydantic import BaseModel

from .message import Message


class ChatModel(BaseModel):
    chat_id: int
    chat_title: str
    chat_messages: list[Message]

    def __str__(self) -> None:
        return f"Chat({self.chat_id}, title={self.chat_title})"

    def get_messages(self) -> list[Message]:
        return self.chat_messages
