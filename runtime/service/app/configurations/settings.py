from pydantic import BaseSettings

class Settings(BaseSettings):
    checkpoint_dir: str = '/app/services/checkpoint/run1'
    MLFLOW_TRACKING_USERNAME: str = "user_name"
    MLFLOW_TRACKING_PASSWORD: str = "password"
    AZURE_STORAGE_CONNECTION_STRING: str = "DefaultEndpointsProtocol=https;AccountName=something;AccountKey=something;EndpointSuffix=something"
    AZURE_ACCESS_KEY: str = 'something'
    QNAMAKER_RUN_ID: str = 'run_id'
    artifact_uri: str = 'mlflow_artifact_uri'

def get_settings():
    return Settings()
