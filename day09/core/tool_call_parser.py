import json

import re

from typing import Any

from core.tool_call import ToolCall

from core.tool_decision import ToolDecision

class ToolCallParser:

    def parse(self, content: str) -> ToolDecision:

        cleaned_content = self._extract_json_text(content)

        try:

            data: dict[str, Any] = json.loads(cleaned_content)

        except json.JSONDecodeError as error:

            raise ValueError(

                f"模型没有返回合法 JSON：{cleaned_content}"

            ) from error

        action = data.get("action")

        if action == "answer":

            return ToolDecision(action="answer")

        if action != "tool":

            raise ValueError(f"未知 action：{action}")

        tool_name = data.get("tool_name")

        arguments = data.get("arguments", {})

        if not isinstance(tool_name, str) or not tool_name.strip():

            raise ValueError("tool_name 必须是非空字符串")

        if not isinstance(arguments, dict):

            raise ValueError("arguments 必须是对象")

        return ToolDecision(

            action="tool",

            tool_call=ToolCall(

                name=tool_name,

                arguments=arguments,

            ),

        )

    @staticmethod

    def _extract_json_text(content: str) -> str:

        content = content.strip()

        # 1. 去掉 MiniMax 返回的思考内容

        content = re.sub(

            r"<think>.*?</think>",

            "",

            content,

            flags=re.DOTALL,

        ).strip()

        # 2. 优先提取 Markdown JSON 代码块

        code_block_match = re.search(

            r"```(?:json)?\s*(\{.*\})\s*```",

            content,

            flags=re.DOTALL,

        )

        if code_block_match:

            return code_block_match.group(1).strip()

        # 3. 没有代码块时，尝试提取最外层 JSON 对象

        json_match = re.search(

            r"\{.*\}",

            content,

            flags=re.DOTALL,

        )

        if json_match:

            return json_match.group(0).strip()

        raise ValueError(f"响应中没有找到 JSON：{content}")