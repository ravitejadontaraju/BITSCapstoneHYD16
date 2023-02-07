from pydantic import BaseModel

class RequestModel(BaseModel):
  input_job_title : str
  input_skills:str
  input_company_name:str
  input_location:str