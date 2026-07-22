from abc import ABC, abstractmethod
from pathlib import Path


class PromptLoader(ABC):

    @abstractmethod
    def load(self, scene: str) -> str:
        """根据场景加载 Prompt。"""
        raise NotImplementedError()