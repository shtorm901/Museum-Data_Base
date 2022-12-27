from fastapi import FastAPI
from sql_base import base_worker
from settings import Base
from routers.workers import work_router

base_worker.set_base_path(Base)

if not base_worker.Base_check():
    base_worker.Base_create('../sql/base.sql')


app = FastAPI()

@app.get("/")
def main_page():
    return {'page': 'Connection is corect'}


app.include_router(work_router, prefix='/workers')