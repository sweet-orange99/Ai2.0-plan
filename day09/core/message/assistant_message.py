from dataclasses import dataclass
from .message import Message

@dataclass
class AssistantMessage(Message):
    @property
    def role(self) -> str:
        return "assistant"
