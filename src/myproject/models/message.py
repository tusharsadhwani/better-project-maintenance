from uuid import UUID
from pydantic import BaseModel

from myproject.models.user import UserModel


class Message(BaseModel):
    message_id: UUID
    text: str
    user: UserModel = None

    @property
    def sender_name(self):
        """Returns the name of the user who sent the message."""
        return self.user.username
