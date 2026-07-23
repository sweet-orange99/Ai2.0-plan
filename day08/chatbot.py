from chat.chat_service import ChatService
from chat.memory import ChatMemory
from llm.minimax_chat_model import MiniMaxChatModel
from prompt.local_prompt_loader import LocalPromptLoader
from prompt.prompt_manager import PromptManager
from prompt.prompt_template import PromptTemplate


def main() -> None:
    prompt_manager = PromptManager(
        loader=LocalPromptLoader(),
        template=PromptTemplate(),
    )

    system_prompt = prompt_manager.load(
        scene="java_chat",
        variables={
            "current_date": "2026-07-22",
            "user_name": "甜澍",
        },
    )

    memory = ChatMemory()
    memory.add_system_message(system_prompt)

    chat_service = ChatService(
        memory=memory,
        chat_model=MiniMaxChatModel(),
    )

    print("=" * 50)
    print("MiniLangChain AI 助手已启动")
    print("输入 exit 或 quit 结束对话")
    print("=" * 50)

    while True:
        user_input = input("\n用户：").strip()

        if not user_input:
            continue

        if user_input.lower() in {"exit", "quit"}:
            print("对话结束。")
            break

        try:
            response = chat_service.chat(user_input)

            print(f"\nAI：{response.content}")
            print(f"模型：{response.model}")
            print(f"Token：{response.usage.get('total_tokens', 0)}")

        except Exception as error:
            print(f"聊天失败：{error}")


if __name__ == "__main__":
    main()