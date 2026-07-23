from dataclasses import dataclass
from .message import Message

@dataclass
class SystemMessage(Message):
    @property
    def role(self) -> str:
        return "system"