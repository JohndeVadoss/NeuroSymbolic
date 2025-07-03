import sys

import pytest

pytest.importorskip("vllm", reason="vLLM not installed or CUDA missing")

from vllm_host import server


def test_build_server_command():
    cmd = server.build_server_command("model", "localhost", 1234)
    assert "--model" in cmd
    assert "model" in cmd
    assert "--port" in cmd
    assert "1234" in cmd
