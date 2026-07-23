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

