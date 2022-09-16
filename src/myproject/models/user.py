from uuid import UUID
from pydantic import BaseModel


class UserModel(BaseModel):
    userid: UUID
    username: str

    def __repr__(self) -> str:
        return f"User({self.userid.hex})"
