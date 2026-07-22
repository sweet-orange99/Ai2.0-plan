from .prompt_loader import PromptLoader
from .prompt_template import PromptTemplate


class PromptManager:
    def __init__(
        self,
        loader: PromptLoader,
        template: PromptTemplate,
    ) -> None:
        self.loader = loader
        self.template = template

    def load(
        self,
        scene: str,
        variables: dict[str, str] | None = None,
    ) -> str:
        prompt_text = self.loader.load(scene)

        return self.template.render(
            template=prompt_text,
            variables=variables,
        )