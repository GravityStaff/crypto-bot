import pytest
import os
from cryptobot.config import load_config

def test_missing_file_raises():
    with pytest.raises(FileNotFoundError):
        load_config("nonexistent.yaml")

def test_minimal_valid_config(tmp_path):
    d = tmp_path / "sub"
    d.mkdir()
    p = d / "config.yaml"
    p.write_text("rpc_url: http://localhost:8545\nprivate_key: 0x123")
    
    cfg = load_config(str(p))
    assert cfg['rpc_url'] == "http://localhost:8545"

# TODO: add checks for malformed yaml
