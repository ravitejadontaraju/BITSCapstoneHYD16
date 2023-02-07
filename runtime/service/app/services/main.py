from Task1_indeedJobScraping import fetch_jobs

from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel

import json

class Item(BaseModel):
    job_title: str

app = FastAPI()


@app.post("/dataset")
async def details(item: Item):
    item_dict = item.dict()
    data = fetch_jobs(item_dict["job_title"])
    data = json.loads(data)
    return {"result": data}
