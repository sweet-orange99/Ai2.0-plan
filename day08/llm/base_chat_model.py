from abc import ABC, abstractmethod

from core.message import Message


class BaseChatModel(ABC):

    @abstractmethod
    def chat(
        self,
        messages: list[Message],
    ) -> str | None:
        """
        根据消息历史调用模型。
        """
        ...