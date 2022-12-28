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


@work_router.get('/{worker_id}')
def get_worker(worker_id: int):
    worker = resolvers.get_worker(worker_id)
    return f'Worker: {{name: имя, surname: фамилия, middle_name: отчество, phone_number: номер телефона, id: {worker_id}}}'



@work_router.put('/{worker_id}')
def update_worker(worker_id: int):
    return f'Update worker {worker_id}'


@work_router.delete('/{worker_id}')
def delete_worker(worker_id: int):
    return f'delete worker {worker_id}'