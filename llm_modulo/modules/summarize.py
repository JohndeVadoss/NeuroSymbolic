from .base import Module

class SummarizeModule(Module):
    """A simple summarization module using a heuristic."""

    def run(self, text: str) -> str:
        """Return the first sentence of the text as summary."""
        for delimiter in [".", "!", "?"]:
            if delimiter in text:
                return text.split(delimiter)[0].strip() + delimiter
        # If no sentence delimiter found, return truncated text
        return text[:50] + ("..." if len(text) > 50 else "")
