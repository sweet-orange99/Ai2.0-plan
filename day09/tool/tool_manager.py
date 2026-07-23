from typing import Any

from .weather_tool import WeatherTool

from .base_tool import BaseTool


class ToolManager:
    def __init__(
        self,
        tools: list[BaseTool] | None = None,
    ) -> None:
        self._tools: dict[str, BaseTool] = {}

        if tools:
            for tool in tools:
                self.register(tool)

    def register(self, tool: BaseTool) -> None:
        if not tool.name:
            raise ValueError("工具名称不能为空")

        if tool.name in self._tools:
            raise ValueError(
                f"工具已存在：{tool.name}"
            )

        self._tools[tool.name] = tool

    def get(self, name: str) -> BaseTool:
        tool = self._tools.get(name)

        if tool is None:
            raise KeyError(f"未找到工具：{name}")

        return tool

    def execute(
        self,
        name: str,
        **kwargs: Any,
    ) -> str:
        tool = self.get(name)
        return tool.execute(**kwargs)

    def list_tools(self) -> list[BaseTool]:
        return list(self._tools.values())

    def build_prompt_description(self) -> str:
        if not self._tools:
            return "当前没有可用工具。"

        return "\n\n".join(
            tool.to_prompt_description()
            for tool in self._tools.values()
        )


