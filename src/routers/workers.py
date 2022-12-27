from fastapi import APIRouter
from sql_base import Hall

worker_router = APIRouter()


@worker_router.post('/')
def new_worker()