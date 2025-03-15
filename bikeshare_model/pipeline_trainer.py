# pipeline_trainer.py
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import joblib
from bikeshare_model.pipeline_builder import build_pipeline
from bikeshare_model.data_manager import load_data
from bikeshare_model.config import TARGET, RANDOM_SEED

def train_pipeline():
    """
    Train the pipeline using the provided dataset and evaluate the performance.
    """
    df = load_data()
    X = df.drop(columns=[TARGET])
    y = df[TARGET]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=RANDOM_SEED)

    pipeline = build_pipeline()
    pipeline.fit(X_train, y_train)

    # Evaluate performance
    y_pred = pipeline.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    print(f"Mean Squared Error: {mse}")
    print(f"R-squared: {r2}")

    # Save the model
    joblib.dump(pipeline, 'bike_sharing_model.pkl')

if __name__ == "__main__":
    train_pipeline()
