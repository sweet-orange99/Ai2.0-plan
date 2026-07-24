from pathlib import Path
from .prompt_loader import PromptLoader

class LocalPromptLoader(PromptLoader):

    def __init__(self, prompt_dir: str | Path | None = None):
        self.prompt_dirs: list[Path]

        if prompt_dir is None:
            base_dir = Path(__file__).parent
            self.prompt_dirs = [
                base_dir / "templates",
                base_dir / "prompts",
            ]
            return

        self.prompt_dirs = [Path(prompt_dir)]

    def load(self, scene: str) -> str:
        for prompt_dir in self.prompt_dirs:
            prompt_path = prompt_dir / f"{scene}.md"

            if prompt_path.exists():
                return prompt_path.read_text(
                    encoding="utf-8"
                )

        raise FileNotFoundError(
            f"Prompt 不存在：{scene}"
        )
