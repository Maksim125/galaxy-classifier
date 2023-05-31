import pytest
from app.dependencies import classifier_proxy
import numpy as np
from app.main import app
from unittest.mock import MagicMock
from fastapi import UploadFile
import io


@pytest.fixture(scope="session")
def test_client():
    from fastapi.testclient import TestClient
    client = TestClient(app)
    yield client

@pytest.fixture(scope = "function")
def classification_result():
    yield np.array([0.85, 0.95, 0.5, 0.5])

@pytest.fixture(scope="function")
def override_tflow_proxy(classification_result):
    async def sample_predict(image):
        return classification_result
    
    app.dependency_overrides[classifier_proxy] = lambda : MagicMock(predict = sample_predict)
    yield

@pytest.fixture(scope = "function")
def test_image_bytes():
    with open("tests/test_image.jpg", "rb") as f:
        yield f.read()

@pytest.fixture(scope="function")
def upload_file_generator(test_image_bytes):
    yield lambda filename, content_type : MockUploadFile(filename = filename, file = io.BytesIO(test_image_bytes), content_type=content_type)

@pytest.fixture(scope="function")
def classification_description():
    classification = {
            1 : "Elliptical",
            2 : "Lenticular",
            3 : "Tight Spiral",
            4 : "Loose Spiral"
        }
    description = {
        1 : "Elliptical galaxies are round and featureless, with little to no star formation.",
        2 : "Lenticular galaxies are disk-shaped, with little to no spiral structure.",
        3 : "Tight spiral galaxies have a well-defined spiral structure, with tightly wound arms.",
        4 : "Loose spiral galaxies have a well-defined spiral structure, with loosely wound arms."
    }
    yield classification, description


class MockUploadFile(UploadFile):
    def __init__(self, filename: str, file: io.BytesIO, content_type: str):
        super().__init__(filename=filename, file=file)
        self._content_type = content_type

    @property
    def content_type(self) -> str:
        return self._content_type
    