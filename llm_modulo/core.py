from typing import List
from .modules import Module, EchoModule, SummarizeModule

class LLMModulo:
    """Lightweight orchestrator that runs a sequence of modules."""

    def __init__(self, modules: List[Module]):
        self.modules = modules

    def run(self, text: str) -> str:
        output = text
        for module in self.modules:
            output = module.run(output)
        return output


def default_pipeline() -> 'LLMModulo':
    """Return a default pipeline with echo and summarization."""
    return LLMModulo([EchoModule(), SummarizeModule()])
