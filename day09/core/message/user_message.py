from dataclasses import dataclass
from .message import Message

@dataclass
class UserMessage(Message):
    @property
    def role(self) -> str:
        return "user"