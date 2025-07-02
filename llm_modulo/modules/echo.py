from .base import Module

class EchoModule(Module):
    """A simple module that echoes the input text."""

    def run(self, text: str) -> str:
        return text
