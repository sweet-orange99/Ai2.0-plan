from pathlib import Path
from .prompt_loader import PromptLoader

class LocalPromptLoader(PromptLoader):

    def __init__(self,prompt_dir: str = "prompt/prompts"):
        self.prompt_dir = Path(prompt_dir)

    def load(self, scene: str) -> str:
        prompt_path = (
            self.prompt_dir
            / f"{scene}.md"
        )
        if not prompt_path.exists():
            raise FileNotFoundError(
                f"Prompt 不存在：{scene}"
            )
        return prompt_path.read_text(
            encoding="utf-8"
        )