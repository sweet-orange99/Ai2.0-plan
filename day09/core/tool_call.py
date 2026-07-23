from dataclasses import dataclass, field
from typing import Any
from uuid import uuid4


@dataclass
class ToolCall:
    name: str
    arguments: dict[str, Any] = field(default_factory=dict)
    id: str = field(
        default_factory=lambda: uuid4().hex
    )