from pydantic import BaseModel

class GalaxyType(BaseModel):
    category : str
    description : str