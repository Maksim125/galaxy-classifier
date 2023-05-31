
def test_classification(test_client, override_tflow_proxy, test_image_bytes):
    
    response = test_client.post(
        "/classify-galaxy", 
        files = {
            "image" : ("image.jpg", test_image_bytes, "image/jpeg")
        }
    )
    assert response.status_code == 200
    assert {"category" : "Lenticular", "confidence" : 0.95}.items() <= response.json().items()
