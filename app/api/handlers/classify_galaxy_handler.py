from app.dto.api_response.galaxy_type import GalaxyType
from fastapi.exceptions import HTTPException
from fastapi import File, UploadFile
from PIL import Image
from typing import Tuple
import io
import numpy as np
from app.proxies.tflow_serving_proxy import TFlowServingProxy


async def classify_galaxy_handler(image, classifier) -> GalaxyType:
    validate_image(image)
    prepared_image = prepare_image(image)
    category_idx, confidence = await classify_image(prepared_image, classifier)
    return GalaxyType.from_classification(category_idx, confidence)


def validate_image(image : UploadFile) -> None:
    if image.content_type not in ["image/jpeg", "image/png"]:
        raise HTTPException(
            status_code = 415,
            detail = "Unsupported file provided. Please provide a JPEG or PNG image.",
        )

def prepare_image(image : UploadFile) -> np.ndarray:
    image_bytes = image.file.read()
    img = Image.open(io.BytesIO(image_bytes))
    img = img.resize((32, 32), Image.BILINEAR)
    img = img.convert("RGB")
    img = np.array(img) / 255.0
    return img

def parse_results(results : np.ndarray) -> Tuple[int, float]:
    category = int(np.argmax(results) + 1)
    return category, results[category - 1]

async def classify_image(image : np.ndarray, classifier : TFlowServingProxy) -> Tuple[int, float]:
    classifier_results = await classifier.predict(image)
    return parse_results(classifier_results)

