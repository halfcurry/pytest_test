import joblib
import pandas as pd
import os
from bikeshare_model.config import TARGET

# Define the model path
MODEL_PATH = "bike_sharing_model.pkl"

def load_model():
    """
    Load the trained model from a file.
    """
    if not os.path.exists(MODEL_PATH):
        raise FileNotFoundError(f"Model file '{MODEL_PATH}' not found. Train the model first.")
    
    return joblib.load(MODEL_PATH)

def make_prediction(input_data):
    """
    Load the trained model and make predictions on new input data.
    """
    model = load_model()
    
    # Convert input to DataFrame if necessary
    if not isinstance(input_data, pd.DataFrame):
        input_data = pd.DataFrame(input_data)

    prediction = model.predict(input_data)
    return prediction

if __name__ == "__main__":
    # Example usage
    sample_input = {
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
    }
    
    df = pd.DataFrame(sample_input)
    print("Prediction:", make_prediction(df))
