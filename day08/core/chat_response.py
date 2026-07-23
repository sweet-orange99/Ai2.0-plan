from dataclasses import dataclass, field
from typing import Any

from core.message import AssistantMessage


@dataclass
class ChatResponse:
    message: AssistantMessage
    model: str | None = None
    finish_reason: str | None = None
    usage: dict[str, int] = field(default_factory=dict)
    metadata: dict[str, Any] = field(default_factory=dict)

    @property
    def content(self) -> str:
        return self.message.content