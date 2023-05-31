from app.dto.api_response.galaxy_type import GalaxyType
import pytest

@pytest.mark.parametrize(
        "category_idx, confidence", [
            (1, 0.95),
            (2, 0.93),
            (3, 0.92),
            (4, 0.91),
            (5, 0.90),
        ]
)
def test_static_constructor(category_idx, confidence, classification_description):
    res = GalaxyType.from_classification(category_idx, confidence)
    classification, description = classification_description

    assert res.category == classification.get(category_idx, "")
    assert res.description == description.get(category_idx, "")
    assert res.confidence == confidence
