from llm_modulo import EchoModule, SummarizeModule, LLMModulo


def test_echo_module():
    echo = EchoModule()
    assert echo.run("hello") == "hello"


def test_pipeline_summary():
    pipeline = LLMModulo([EchoModule(), SummarizeModule()])
    text = "Sentence one. Sentence two."
    assert pipeline.run(text) == "Sentence one."
