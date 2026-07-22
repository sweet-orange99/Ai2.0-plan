from openai import APIConnectionError, APIStatusError, OpenAI

from config import (
    MINIMAX_API_KEY,
    MINIMAX_BASE_URL,
    MINIMAX_MODEL,
)
from core.message import Message


class MiniMaxChatbot:
    def __init__(
        self,
        api_key: str | None = None,
        base_url: str | None = None,
        model: str | None = None,
    ) -> None:
        self.api_key = api_key or MINIMAX_API_KEY
        self.base_url = base_url or MINIMAX_BASE_URL
        self.model = model or MINIMAX_MODEL

        if not self.api_key:
            raise ValueError(
                "未找到 MINIMAX_API_KEY，请检查 .env 文件"
            )

        self.client = OpenAI(
            api_key=self.api_key,
            base_url=self.base_url,
        )

    def chat(
        self,
        messages: list[Message],
    ) -> str | None:
        try:
            sdk_messages = [
                message.to_dict()
                for message in messages
            ]

            response = self.client.chat.completions.create(
                model=self.model,
                messages=sdk_messages,
            )

            content = response.choices[0].message.content

            if not content:
                print("模型没有返回文本内容。")
                return None

            return content

        except APIConnectionError as error:
            print(f"网络连接失败：{error}")
            return None

        except APIStatusError as error:
            print(f"API 调用失败，状态码：{error.status_code}")
            print(f"响应内容：{error.response.text}")
            return None

        except Exception as error:
            print(f"发生未知错误：{error}")
            return None