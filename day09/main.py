from chat.chat_service import ChatService
from chat.memory import ChatMemory
from llm.minimax_chat_model import MiniMaxChatModel
from prompt.local_prompt_loader import LocalPromptLoader
from prompt.prompt_manager import PromptManager
from prompt.prompt_template import PromptTemplate
from tool.tool_manager import ToolManager
from tool.weather_tool import WeatherTool
from core.tool_call_parser import ToolCallParser
from core.message.system_message import SystemMessage
from core.message.user_message import UserMessage


def main() -> None:
    prompt_manager = PromptManager(
        loader=LocalPromptLoader(),
        template=PromptTemplate(),
    )
    tool_manager = ToolManager(
        tools=[
            WeatherTool(),
        ]
    )
    router_prompt = prompt_manager.load(
        scene="tool_router",
        variables={
            "tool_descriptions": tool_manager.build_prompt_description(),
        },
    )

    chat_prompt = prompt_manager.load(
        scene="java_chat",
        variables={
            "current_date": "2026-07-23",
            "user_name": "甜澍",
        },
    )

    memory = ChatMemory()
    memory.add_system_message(chat_prompt)


    chat_model = MiniMaxChatModel()
    chat_service = ChatService(
        memory=memory,
        chat_model=chat_model,
    )

    print("=" * 50)
    print("MiniLangChain AI 助手已启动")
    print("输入 exit 或 quit 结束对话")
    print("=" * 50)
    tool_call_parser = ToolCallParser()

    while True:
        user_input = input("\n用户：").strip()

        if not user_input:
            continue

        if user_input.lower() in {"exit", "quit"}:
            print("对话结束。")
            break

        try:
            router_messages = [
                SystemMessage(content=router_prompt),
                UserMessage(content=user_input),
            ]

            router_response = chat_model.chat(router_messages)
            decision = tool_call_parser.parse(router_response.content)

            if not decision.requires_tool:
                response = chat_service.chat(user_input)
                print(f"\nAI：{response.content}")
                continue

            tool_call = decision.tool_call

            if tool_call is None:
                raise ValueError("工具决策缺少 tool_call")

            tool_result = tool_manager.execute(
                name=tool_call.name,
                **tool_call.arguments,
            )

            memory.add_user_message(user_input)
            memory.add_user_message(
                f"""
    工具 `{tool_call.name}` 的执行结果：

    {tool_result}

    请严格根据该结果回答用户，不得编造额外信息。
    """.strip()
            )

            response = chat_model.chat(
                memory.get_messages()
            )

            memory.add_assistant_message(
                response.content
            )

            print(f"\nAI：{response.content}")

        except Exception as error:
            print(f"聊天失败：{error}")


if __name__ == "__main__":
    main()