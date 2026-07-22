from chat.memory import ChatMemory
from llm.minimax_chat import MiniMaxChatbot
from prompt.local_prompt_loader import LocalPromptLoader
from prompt.prompt_manager import PromptManager
from prompt.prompt_template import PromptTemplate


def main() -> None:
    prompt_loader = LocalPromptLoader()
    prompt_template = PromptTemplate()

    prompt_manager = PromptManager(
        loader=prompt_loader,
        template=prompt_template,
    )

    chatbot = MiniMaxChatbot()
    memory = ChatMemory()

    system_prompt = prompt_manager.load(
        scene="java_chat",
        variables={
            "current_date": "2026-07-22",
            "user_name": "甜澍",
        },
    )

    memory.add_system_message(system_prompt)

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

        memory.add_user_message(user_input)

        response = chatbot.chat(
            memory.get_messages()
        )

        if response is None:
            memory.remove_last_message()
            print("未收到模型的有效响应，请重试。")
            continue

        print(f"\nAI:{response}")

        memory.add_assistant_message(response)


if __name__ == "__main__":
    main()