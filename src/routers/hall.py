from fastapi import APIRouter
from sql_base import Hall
import resolvers.hall

hall_router = APIRouter()


@hall_router.get('/')
def get_hall():
    return f'Response: {{text: Страница со списком залов}}'

@hall_router.post('/')
def new_hall(hall: Hall):
    new_id = resolvers.hall.new_hall(hall)
    return f'{{code: 201, id: {new_id}}}'
