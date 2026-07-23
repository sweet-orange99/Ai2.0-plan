from dataclasses import dataclass
from .message import Message

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