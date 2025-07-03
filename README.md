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
- `vllm_host/` – small project for hosting an open source LLM with vLLM.

## Usage

Install dependencies and run the example:

```bash
pip install -r requirements.txt
python run_example.py
```

### Run the vLLM Server

The `vllm_host` package provides a small script to serve an open source model
using vLLM. The default model is `sshleifer/tiny-gpt2`. Launch the server with:

```bash
python -m vllm_host.server --model sshleifer/tiny-gpt2 --port 8000
```
This requires a GPU with CUDA libraries available.

Run the tests with:

```bash
pytest
```
