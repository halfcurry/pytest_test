from bikeshare_model.feature_engineering import preprocess_data
import pandas as pd

def test_preprocess_data():
    sample_data = pd.DataFrame({
        "temp": [0.3, 0.5],
        "atemp": [0.31, 0.48],
        "hum": [0.8, 0.65],
        "windspeed": [0.2, 0.1],
        "casual": [50, 80],
        "registered": [200, 400],
        "season": [1, 2],
        "hr": [10, 15],
        "holiday": [0, 1],
        "weekday": [2, 4],
        "workingday": [1, 0],
        "weathersit": [1, 2]
    })

    processed_data = preprocess_data(sample_data)
    assert processed_data is not None
    assert processed_data.shape[0] == 2  # Ensure data is transformed correctly
