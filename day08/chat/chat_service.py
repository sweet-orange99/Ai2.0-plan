from chat.memory import ChatMemory
from llm.base_chat_model import BaseChatModel


class ChatService:
    def __init__(
        self,
        memory: ChatMemory,
        chat_model: BaseChatModel,
    ) -> None:
        self.memory = memory
        self.chat_model = chat_model

    def chat(self, user_input: str) -> str | None:
        self.memory.add_user_message(user_input)

        response = self.chat_model.chat(
            self.memory.get_messages()
        )

        if response is None:
            self.memory.remove_last_message()
            return None

        self.memory.add_assistant_message(response)

        return response