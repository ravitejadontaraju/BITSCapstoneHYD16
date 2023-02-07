from typing import Dict
from fastapi import APIRouter
import os

import logging

from app.services.model_output_generator import *

from app.schemas.request_body import RequestModel

from app.configurations.settings import get_settings
from app.services.mlflow_model_loader import load_model_mlflow


router = APIRouter(
    prefix='/job_description_generator'
)

#initializing logging
my_logger = logging.getLogger()
my_logger.setLevel(logging.DEBUG)
logging.basicConfig(level=logging.DEBUG, filename='logs.log')


@router.on_event("startup")
#Returns a compiled model identical to the saved after trained
def load_saved_model():
  print('startup')

  # load model
  # try:
  #   print('loading model from mlflow')
  #   os.environ['MLFLOW_TRACKING_USERNAME'] = get_settings().MLFLOW_TRACKING_USERNAME
  #   os.environ['MLFLOW_TRACKING_PASSWORD'] = get_settings().MLFLOW_TRACKING_PASSWORD
  #   os.environ['AZURE_STORAGE_CONNECTION_STRING'] = get_settings().AZURE_STORAGE_CONNECTION_STRING
  #   os.environ['AZURE_ACCESS_KEY'] = get_settings().AZURE_ACCESS_KEY
  #   load_model_mlflow()
  # except:
  #   print('not able to load model from mlflow')
  print('loading model from mlflow')
  os.environ['MLFLOW_TRACKING_USERNAME'] = get_settings().MLFLOW_TRACKING_USERNAME
  os.environ['MLFLOW_TRACKING_PASSWORD'] = get_settings().MLFLOW_TRACKING_PASSWORD
  os.environ['AZURE_STORAGE_CONNECTION_STRING'] = get_settings().AZURE_STORAGE_CONNECTION_STRING
  os.environ['AZURE_ACCESS_KEY'] = get_settings().AZURE_ACCESS_KEY
  load_model_mlflow()

@router.post("/predictJobDescription") 
async def predictJobDescription(request_model:RequestModel):
  jobDescription = getModelOutputSingleInput(request_model.input_job_title,
                                              request_model.input_skills,
                                              request_model.input_company_name,
                                              request_model.input_location)
  return jobDescription