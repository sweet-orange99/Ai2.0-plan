from dataclasses import dataclass
from abc import ABC, abstractmethod

@dataclass
class Message(ABC):
    content: str

    @property
    @abstractmethod
    def role(self) -> str:
        raise NotImplementedError

    def to_dict(self) -> dict[str, str]:
        return {
            "role": self.role,
            "content": self.content,
        }
    def remove_last_message(self) -> Message | None:
        if not self._messages:
            return None

        return self._messages.pop()
@dataclass
class SystemMessage(Message):
    @property
    def role(self) -> str:
        return "system"


@dataclass
class UserMessage(Message):
    @property
    def role(self) -> str:
        return "user"


@dataclass
class AssistantMessage(Message):
    @property
    def role(self) -> str:
        return "assistant"


@dataclass
class ToolMessage(Message):
    tool_call_id: str

    @property
    def role(self) -> str:
        return "tool"

    def to_dict(self) -> dict[str, str]:
        return {
            "role": self.role,
            "content": self.content,
            "tool_call_id": self.tool_call_id,
        }