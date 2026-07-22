from prompt.prompt_template import PromptTemplate
from prompt.prompt_manager import PromptManager
from prompt.local_prompt_loader import LocalPromptLoader

def main()-> None:
    prompt_loader = LocalPromptLoader()
    prompt_template = PromptTemplate()
    prompt_manager = PromptManager(prompt_loader,prompt_template)
    prompt = prompt_manager.load(
        scene="java_chat",
        variables={
            "current_date": "2026-07-22",
            "user_name": "甜澍",
        },)
    print(prompt)

    message = Message()
if __name__ == "__main__":
    main()