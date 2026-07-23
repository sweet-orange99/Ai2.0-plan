from typing import Any

from .base_tool import BaseTool


class WeatherTool(BaseTool):
    name = "get_weather"
    description = "查询指定城市的天气"

    parameters = {
        "city": {
            "type": "string",
            "description": "需要查询天气的城市名称",
            "required": True,
        }
    }

    def execute(self, **kwargs: Any) -> str:
        city = kwargs.get("city")

        if not isinstance(city, str) or not city.strip():
            raise ValueError("city 必须是非空字符串")

        return f"{city}天气晴，温度25℃"