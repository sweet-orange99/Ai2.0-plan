class PromptTemplate:
    def render(
        self,
        template: str,
        variables: dict[str, str] | None = None,
    ) -> str:
        if not variables:
            return template

        return template.format(**variables)