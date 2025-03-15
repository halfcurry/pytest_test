# feature_engineering.py
import pandas as pd
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.base import BaseEstimator, TransformerMixin

class WeekdayImputer(BaseEstimator, TransformerMixin):
    def fit(self, X, y=None):
        return self

    def transform(self, X):
        # Implement the logic for imputing weekday based on the dteday column
        X = X.copy()
        X['weekday'] = pd.to_datetime(X['dteday']).dt.weekday
        return X

def build_feature_pipeline():
    """
    Build feature engineering pipeline with transformations for numerical and categorical features.
    """
    num_features = ['temp', 'atemp', 'hum', 'windspeed', 'casual', 'registered']
    cat_features = ['season', 'hr', 'holiday', 'weekday', 'workingday', 'weathersit']

    num_pipeline = Pipeline([
        ('imputer', SimpleImputer(strategy='mean')),
        ('scaler', StandardScaler())
    ])

    cat_pipeline = Pipeline([
        ('imputer', SimpleImputer(strategy='most_frequent')),
        ('one_hot', OneHotEncoder(handle_unknown='ignore'))
    ])

    preprocessor = ColumnTransformer([
        ('num', num_pipeline, num_features),
        ('cat', cat_pipeline, cat_features)
    ])
    
    return preprocessor

def preprocess_data(df):
    """
    Apply the feature pipeline transformations to the input DataFrame.
    """
    pipeline = build_feature_pipeline()
    df_transformed = pipeline.fit_transform(df)
    return df_transformed
