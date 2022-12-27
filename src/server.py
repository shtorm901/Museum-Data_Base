from fastapi import FastAPI
from sql_base import base_worker
from settings import Base


base_worker.set_base_path(Base)

if not base_worker.Base_check():
    base_worker.Base_create('../sql/base.sql')


app = FastAPI()
