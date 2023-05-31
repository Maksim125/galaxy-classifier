from pydantic import BaseModel

class GalaxyType(BaseModel):
    category : str
    description : str
    confidence : float

    @classmethod
    def from_classification(cls, class_idx : int, confidence : float) -> "GalaxyType":
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

        return cls(
            category = classification.get(class_idx, ""),
            description = description.get(class_idx, ""),
            confidence = confidence)
