from pathlib import Path


class PromptLoader:

    def __init__(self, prompt_dir="prompt/prompts"):
        self.prompt_dir = Path(prompt_dir)

    def load(self, prompt_name: str) -> str:
        prompt_file = self.prompt_dir / f"{prompt_name}.md"

        return prompt_file.read_text(
            encoding="utf-8"
        )