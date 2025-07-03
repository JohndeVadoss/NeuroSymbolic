"""Simple wrapper to launch a vLLM OpenAI-style server."""

from __future__ import annotations

import argparse
import subprocess
from typing import List


DEF_MODEL = "sshleifer/tiny-gpt2"


def build_server_command(model: str, host: str, port: int) -> List[str]:
    """Return the command to start the vLLM server."""
    return [
        "python",
        "-m",
        "vllm.entrypoints.api_server",
        "--model",
        model,
        "--host",
        host,
        "--port",
        str(port),
    ]


def start_server(model: str = DEF_MODEL, host: str = "0.0.0.0", port: int = 8000) -> None:
    """Start the vLLM server with the given model."""
    cmd = build_server_command(model, host, port)
    subprocess.run(cmd, check=True)


def main() -> None:
    parser = argparse.ArgumentParser(description="Start a vLLM server")
    parser.add_argument("--model", default=DEF_MODEL)
    parser.add_argument("--host", default="0.0.0.0")
    parser.add_argument("--port", type=int, default=8000)
    args = parser.parse_args()
    start_server(args.model, args.host, args.port)


if __name__ == "__main__":
    main()
