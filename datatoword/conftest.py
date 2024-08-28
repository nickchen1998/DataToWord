import os
import pytest
from dotenv import load_dotenv
from pathlib import Path


@pytest.fixture()
def openai_api_key() -> str:
    if os.getenv("OPENAI_API_KEY"):
        openai_api_key = os.getenv("OPENAI_API_KEY")
    else:
        load_dotenv(Path(__file__).resolve().parent.parent / ".env")
        openai_api_key = os.getenv("OPENAI_API_KEY")

    if openai_api_key is None:
        raise ValueError("pass openai_api_key or set OPENAI_API_KEY in environment variable")

    return openai_api_key
