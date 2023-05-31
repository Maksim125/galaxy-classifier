import os
import httpx
import numpy as np

class TFlowServingProxy:
    def __init__(self):
        self._tflow_address = f"http://{os.environ.get('MODEL_HOST', 'model')}:{os.environ.get('MODEL_PORT', '8501')}/v1/models/{os.environ.get('MODEL_NAME', 'galaxy-classifier')}:predict"

    async def predict(self, image_arr : np.ndarray):
        async with httpx.AsyncClient() as client:
            response = await client.post(
                self._tflow_address,
                json = {
                    "signature_name": "serving_default",
                    "instances": [
                        {
                            "input_45": image_arr.tolist()
                        }
                    ]
                },
            )
        response.raise_for_status()

        return response.json()["predictions"][0]
    