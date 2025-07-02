class Module:
    """Base class for modules in the LLM-Modulo framework."""
    def run(self, text: str) -> str:
        raise NotImplementedError("Module subclasses must implement run().")
