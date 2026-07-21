from prompt_template import PromptTemplate
from prompts import SYSTEM_TEMPLATE


def build_system_prompt(
    role,
    task,
    constraint,
):
    template = PromptTemplate(SYSTEM_TEMPLATE)

    return template.format(
        role=role,
        task=task,
        constraint=constraint,
    )