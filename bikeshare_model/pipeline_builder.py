# pipeline_builder.py
from sklearn.ensemble import RandomForestRegressor
from sklearn.pipeline import Pipeline
from bikeshare_model.feature_engineering import build_feature_pipeline

def build_pipeline():
    """
    Build the full pipeline: feature processing and regressor.
    """
    preprocessor = build_feature_pipeline()

    pipeline = Pipeline([
        ('preprocessor', preprocessor),
        ('regressor', RandomForestRegressor(n_estimators=100, random_state=42))
    ])
    
    return pipeline
