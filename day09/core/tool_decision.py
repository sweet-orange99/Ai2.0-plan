from dataclasses import dataclass

from .tool_call import ToolCall


@dataclass
class ToolDecision:
    action: str
    tool_call: ToolCall | None = None

    @property
    def requires_tool(self) -> bool:
        return self.action == "tool"