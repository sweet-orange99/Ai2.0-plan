from abc import ABC, abstractmethod
from typing import Any


class BaseTool(ABC):
    name: str
    description: str
    parameters: dict[str, Any]

    @abstractmethod
    def execute(self, **kwargs: Any) -> str:
        ...

    def to_prompt_description(self) -> str:
        return (
            f"工具名称：{self.name}\n"
            f"工具用途：{self.description}\n"
            f"参数定义：{self.parameters}"
        )