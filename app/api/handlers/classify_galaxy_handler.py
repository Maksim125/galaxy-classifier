from app.dto.api_response.galaxy_type import GalaxyType


async def classify_galaxy_handler(image):
    return GalaxyType(category = "spiral", description = "This is a spiral galaxy")
