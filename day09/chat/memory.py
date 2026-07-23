from core.message.message import Message
from core.message.system_message import SystemMessage
from core.message.assistant_message import AssistantMessage
from core.message.user_message import UserMessage
from core.message.tool_message import ToolMessage


class ChatMemory:
    def __init__(self) -> None:
        self._messages: list[Message] = []

    def add_system_message(self, content: str) -> None:
        self._messages.append(
            SystemMessage(content=content)
        )

    def add_user_message(self, content: str) -> None:
        self._messages.append(
            UserMessage(content=content)
        )

    def add_assistant_message(self, content: str) -> None:
        self._messages.append(
            AssistantMessage(content=content)
        )

    def get_messages(self) -> list[Message]:
        return self._messages.copy()

    def remove_last_message(self) -> Message | None:
        if not self._messages:
            return None
        return self._messages.pop()

    def clear(self) -> None:
        self._messages.clear()

    def to_dict_list(self) -> list[dict[str, str]]:
        return [
            message.to_dict()
            for message in self._messages
        ]
    def add_tool_message(

        self,

        content: str,

        tool_call_id: str,

    ) -> None:

        self._messages.append(

            ToolMessage(

                content=content,

                tool_call_id=tool_call_id,

            )

        )