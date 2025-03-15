# data_manager.py
import pandas as pd
from bikeshare_model.config import DATA_PATH

def load_data():
    """
    Load dataset from the given path.
    """
    return pd.read_csv(DATA_PATH)

def handle_missing_values(df):
    """
    Handle missing values in the dataframe.
    """
    # Your code for handling missing values (using imputation classes)
    pass
