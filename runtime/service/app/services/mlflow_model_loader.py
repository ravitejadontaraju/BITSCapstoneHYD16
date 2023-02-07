import mlflow
import os
from pathlib import Path
from app.configurations.settings import get_settings

os.environ['MLFLOW_TRACKING_USERNAME'] = get_settings().MLFLOW_TRACKING_USERNAME
os.environ['MLFLOW_TRACKING_PASSWORD'] = get_settings().MLFLOW_TRACKING_PASSWORD
os.environ['AZURE_STORAGE_CONNECTION_STRING'] = get_settings().AZURE_STORAGE_CONNECTION_STRING
os.environ['AZURE_ACCESS_KEY'] = get_settings().AZURE_ACCESS_KEY


mlflow.tracking.set_tracking_uri("http://mltracking.deepailytics.com/")

def load_model_mlflow():
    mlflow.set_experiment('job-desc-generator')
    RESOURCE_PATH = os.getcwd() + '/app/services/checkpoint'
    file_path = Path(os.path.join(RESOURCE_PATH))
    
    if ~file_path.exists():
        mlflow.artifacts.download_artifacts(artifact_uri=get_settings().artifact_uri, dst_path=file_path)