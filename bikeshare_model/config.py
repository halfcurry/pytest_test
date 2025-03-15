# config.py
DATA_PATH = 'bike-sharing-dataset.csv'  # Example path to your dataset
TARGET = 'cnt'  # The target column name
NUM_FEATURES = ['temp', 'atemp', 'hum', 'windspeed', 'casual', 'registered']
CAT_FEATURES = ['season', 'hr', 'holiday', 'weekday', 'workingday', 'weathersit']
RANDOM_SEED = 42
