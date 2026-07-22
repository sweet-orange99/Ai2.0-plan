from prompt.prompt_manager import PromptManager

def main()-> None:
    prompt_manager = PromptManager()
    prompt = prompt_manager.load(scene="java_chat")
    print(prompt)
if __name__ == "__main__":
    main()