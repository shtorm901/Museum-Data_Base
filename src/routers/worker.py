from fastapi import APIRouter
from sql_base import Workers
import resolvers.worker

work_router = APIRouter()


@work_router.get('/')
def get_workers():
    return f'Response: {{text: Страница со списком работников}}'

@work_router.post('/')
def new_workers(workers: Workers):
    new_id = resolvers.worker.new_workers(workers)
    return f'{{code: 201, id: {new_id}}}'