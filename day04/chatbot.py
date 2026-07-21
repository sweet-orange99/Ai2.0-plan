from prompt_service import build_system_prompt
from llm import MiniMaxChatbot

def main()-> None:
    mini_max_chatbot = MiniMaxChatbot()
    system_prompt = build_system_prompt(
        role="Java架构师",
        task="帮助用户解决Java开发问题",
        constraint="""
    回答控制在 200 字以内。
    必须给出 Java 示例代码。
    使用 Markdown 格式回答。
    """.strip(),
    )
    messages = [
        {"role": "system", "content": system_prompt},
    ]
    print("=" * 50)

    print("MiniMax AI 助手已启动")

    print("输入 exit 或 quit 结束对话")

    print("=" * 50)

    while True:
        user_input = input("用户: ").strip()
        if not user_input:
            continue
        if user_input.lower() in {"exit", "quit"}:
            print("对话结束。")
            break

        messages.append({"role": "user", "content": user_input})

        response = mini_max_chatbot.chat(messages)
        if response is None:
            messages.pop()
            print("未收到模型的有效响应，请重试。")
            continue
        print("AI: ")
        print(response)

        messages.append({"role": "assistant", "content": response})

if __name__ == "__main__":
    main()