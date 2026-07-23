from abc import ABC, abstractmethod
from core.chat_response import ChatResponse
from core.message.message import Message



class BaseChatModel(ABC):

    @abstractmethod
    def chat(
        self,
        messages: list[Message],
    ) -> ChatResponse | None:
        ...