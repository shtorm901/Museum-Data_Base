from fastapi import APIRouter
from sql_base.models import Hall
import resolvers.hall as res_hall

hall_router = APIRouter()


@hall_router.get('/')
def get_hall():
    return f'Response: {{text: Страница со списком залов}}'

@hall_router.post('/create')
def new_hall(hall: Hall):
    hall_id = res_hall.new_hall(hall)
    return f'{{code: 201, id: {hall_id}}}'


@hall_router.get('/{hall_id}')
def get_hall(hall_id: int):
    hall = res_hall.get_hall(hall_id)
    return f'{{title_hall: название зала, floor: номер этажа, id:{hall_id}}}'


@hall_router.put('/{hall_id}')
def update_hall(hall_id: int):
    return f'Update hall {hall_id}'


@hall_router.delete('/{hall_id}')
def delete_hall(hall_id: int):
    return f'delete hall {hall_id}'