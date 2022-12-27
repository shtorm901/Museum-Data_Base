from fastapi import APIRouter
from sql_base.models import Workers
import resolvers.workers

work_router = APIRouter()


@work_router.get('/')
def get_workers():
    return f'Response: {{text: Страница со списком работников}}'

@work_router.post('/')
def new_worker(worker: Workers):
    new_id = resolvers.subject.new_worker(worker)
    return f'{{code: 201, id:{new_id}}}'
