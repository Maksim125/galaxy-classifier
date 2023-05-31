from fastapi import APIRouter, File, UploadFile, Depends
from app.api.handlers.classify_galaxy_handler import classify_galaxy_handler
from app.dto.api_response.galaxy_type import GalaxyType
from app.dependencies import classifier_proxy
from typing import Type
from app.proxies.tflow_serving_proxy import TFlowServingProxy

router = APIRouter()

@router.post("/classify-galaxy", response_model = GalaxyType)
async def classify_galaxy(
    image : UploadFile = File(...),
    classifier : Type[TFlowServingProxy] = Depends(classifier_proxy),
    ):
    return await classify_galaxy_handler(image, classifier)
