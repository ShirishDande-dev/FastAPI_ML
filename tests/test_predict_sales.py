
import pytest

PREDICT_ENDPOINT = "/predict"
BATCH_PREDICT_ENDPOINT = "/predict_batch"

from fastapi.testclient import TestClient
from src.app import app

@pytest.fixture(scope="function")
def client():

    with TestClient(app) as c:
        yield c
        # Cleanup if necessary

@pytest.mark.asyncio
async def test_predict_sales(client):

    # Sample input data
    data = {
        "Weight": 9.3,
        "ProductVisibility": 0.016047301,
        "MRP": 249.8092,
        "EstablishmentYear": 1999,
        "ProductID": "FDX07",
        "FatContent": "Low Fat",
        "ProductType": "Snack Foods",
        "OutletID": "OUT045",
        "OutletSize": "Medium",
        "LocationType": "Tier 2",
        "OutletType": "Supermarket Type1"
    }

    # Make a POST request to the predict endpoint
    response = client.post(PREDICT_ENDPOINT, json=data)

    # Check if the response is successful
    assert response.status_code == 200

    # Check if the prediction is in the response
    prediction = response.json()
    assert 'predicted OutletSales' in prediction

    # Optionally, check if the prediction is of the expected type (e.g., float)
    assert isinstance(prediction['predicted OutletSales'], float)


@pytest.mark.asyncio
async def test_predict_batch_sales(client):
    # Sample batch input data
    batch_data = [
        {
            "Weight": 9.3,
            "ProductVisibility": 0.016047301,
            "MRP": 249.8092,
            "EstablishmentYear": 1999,
            "ProductID": "FDX07",
            "FatContent": "Low Fat",
            "ProductType": "Snack Foods",
            "OutletID": "OUT045",
            "OutletSize": "Medium",
            "LocationType": "Tier 2",
            "OutletType": "Supermarket Type1"
        },
        {
            "Weight": 5.0,
            "ProductVisibility": 0.0,
            "MRP": 142.0000,
            "EstablishmentYear": 1985,
            "ProductID": "FDX07",
            "FatContent": "Low Fat",
            "ProductType": "Snack Foods",
            "OutletID": "OUT017",
            "OutletSize": "Medium",
            "LocationType": "Tier 3",
            "OutletType": "Supermarket Type1"
        }
    ]

    # Make a POST request to the predict_batch endpoint
    response = client.post(BATCH_PREDICT_ENDPOINT, json=batch_data)

    # Check if the response is successful
    assert response.status_code == 200

    # Check if the predictions are in the response
    prediction = response.json()
    assert 'predicted OutletSales' in prediction

    # Optionally, check if the predictions are of the expected type (e.g., list of floats)
    assert isinstance(prediction['predicted OutletSales'], list)
    assert all(isinstance(pred, float) for pred in prediction['predicted OutletSales'])

