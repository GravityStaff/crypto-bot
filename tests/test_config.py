import pytest
import os
from cryptobot.config import load_config

def test_missing_file_raises():
    with pytest.raises(FileNotFoundError):
        load_config("nonexistent.yaml")

