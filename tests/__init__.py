from app.main import app
import pytest
from fastapi.testclient import TestClient


@pytest.fixture(scope = "session")
def client():
    return TestClient(app)

