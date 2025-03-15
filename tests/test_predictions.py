import pandas as pd
import pytest
from bikeshare_model.predict import make_prediction

@pytest.fixture
def sample_input():
    return pd.DataFrame({
        "temp": [0.3],
        "atemp": [0.31],
        "hum": [0.8],
        "windspeed": [0.2],
        "casual": [50],
        "registered": [200],
        "season": [1],
        "hr": [10],
        "holiday": [0],
        "weekday": [2],
        "workingday": [1],
        "weathersit": [1]
    })

def test_make_prediction(sample_input):
    try:
        prediction = make_prediction(sample_input)
        assert prediction is not None
        assert len(prediction) == 1  # Ensure single prediction is returned
    except FileNotFoundError:
        pytest.skip("Model file not found. Train the model first.")
