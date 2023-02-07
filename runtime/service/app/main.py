from fastapi import FastAPI
import logging
from app.routers import jd_generator

app = FastAPI(title="Job Description Generator API", description="Job Description Generator")

#initializing logging
my_logger = logging.getLogger()
my_logger.setLevel(logging.DEBUG)
logging.basicConfig(level=logging.DEBUG, filename='logs.log')

app.include_router(jd_generator.router)