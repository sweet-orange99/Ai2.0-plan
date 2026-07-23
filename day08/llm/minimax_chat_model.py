from openai import APIConnectionError, APIStatusError, OpenAI

from config import (
    MINIMAX_API_KEY,
    MINIMAX_BASE_URL,
    MINIMAX_MODEL,
)
from core.message import Message,AssistantMessage
from core.chat_response import ChatResponse

class MiniMaxChatModel:
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

    ) -> ChatResponse:

        sdk_messages = [

            message.to_dict()

            for message in messages

        ]

        response = self.client.chat.completions.create(

            model=self.model,

            messages=sdk_messages,

        )

        choice = response.choices[0]

        content = choice.message.content

        if not content:

            raise ValueError("模型没有返回文本内容")

        usage: dict[str, int] = {}

        if response.usage:

            usage = {

                "prompt_tokens": response.usage.prompt_tokens,

                "completion_tokens": response.usage.completion_tokens,

                "total_tokens": response.usage.total_tokens,

            }

        return ChatResponse(

            message=AssistantMessage(content=content),

            model=response.model,

            finish_reason=choice.finish_reason,

            usage=usage,

        )