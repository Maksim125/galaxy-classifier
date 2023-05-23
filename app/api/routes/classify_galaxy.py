from fastapi import APIRouter, File, UploadFile
from app.api.handlers.classify_galaxy_handler import classify_galaxy_handler
from app.dto.api_response.galaxy_type import GalaxyType


router = APIRouter()

@router.post("/classify_galaxy", response_model = GalaxyType)
async def classify_galaxy(
    image : UploadFile = File(...),
    ):
    return await classify_galaxy_handler(image)
