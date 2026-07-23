from chat.memory import ChatMemory
from core.chat_response import ChatResponse
from llm.base_chat_model import BaseChatModel


class ChatService:
    def __init__(
        self,
        memory: ChatMemory,
        chat_model: BaseChatModel,
    ) -> None:
        self.memory = memory
        self.chat_model = chat_model

    def chat(self, user_input: str) -> ChatResponse:
        self.memory.add_user_message(user_input)

        try:
            response = self.chat_model.chat(
                self.memory.get_messages()
            )
        except Exception:
            self.memory.remove_last_message()
            raise

        self.memory.add_assistant_message(
            response.content
        )

        return response