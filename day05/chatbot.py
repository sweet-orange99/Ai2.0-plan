from llm import MiniMaxChatbot
from prompt_loader import PromptLoader

def main()-> None:
    mini_max_chatbot = MiniMaxChatbot()
    loader = PromptLoader()
    system_prompt = loader.load("java_chat")
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