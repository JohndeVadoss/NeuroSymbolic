# NeuroSymbolic

This repository contains a minimal prototype of the **LLM-Modulo** framework.
The goal is to demonstrate how a language model can orchestrate multiple
symbolic modules.  The implementation is intentionally lightweight and does not
rely on any external APIs.

## Directory Structure

- `llm_modulo/` – core library implementing modules and the orchestrator.
- `run_example.py` – small example that runs a default pipeline.
- `tests/` – unit tests verifying basic functionality.
- `requirements.txt` – Python dependencies.

## Usage

Install dependencies and run the example:

```bash
pip install -r requirements.txt
python run_example.py
```

Run the tests with:

```bash
pytest
```
