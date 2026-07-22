from prompt.prompt_loader import PromptLoader


class PromptManager:

    def __init__(self):
        self.loader = PromptLoader()

    def load(
        self,
        scene: str,
        variables=None,
    ) -> str:

        prompt = self.loader.load(scene)

        return prompt