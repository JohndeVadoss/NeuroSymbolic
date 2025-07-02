from llm_modulo import default_pipeline


def main():
    pipeline = default_pipeline()
    text = (
        "The LLM-Modulo framework allows modular reasoning. "
        "This short example shows a simple pipeline."
    )
    result = pipeline.run(text)
    print("Input: ", text)
    print("Output:", result)


if __name__ == "__main__":
    main()
