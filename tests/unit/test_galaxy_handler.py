from app.api.handlers.classify_galaxy_handler import validate_image, prepare_image, parse_results
from fastapi.exceptions import HTTPException
import pytest


def test_image_jpeg(upload_file_generator):
    file = upload_file_generator(filename = "test.jpg", content_type = "image/jpeg")
    validate_image(file)

def test_image_png(upload_file_generator):
    file = upload_file_generator(filename = "test.png", content_type = "image/png")
    validate_image(file)

def test_image_svg(upload_file_generator):
    file = upload_file_generator(filename = "test.svg", content_type = "image/svg+xml")
    with pytest.raises(HTTPException):
        validate_image(file)

def test_image_prepare(upload_file_generator):
    file = upload_file_generator(filename = "test.jpg", content_type = "image/jpeg")

    image = prepare_image(file)

    assert image.shape == (32, 32, 3)
    assert max(image.flatten()) <= 1.0
    assert min(image.flatten()) >= 0.0

def test_parse_results(classification_result):
    results = parse_results(classification_result)
    assert results == (2, 0.95)
