from fastapi import APIRouter
from sql_base import Excursion
import resolvers.excursion

exc_router = APIRouter()


@exc_router.get('/')
def get_excursion():
    return f'Response: {{text: Страница со списком экскурсий}}'

@exc_router.post('/')
def new_excursion(excursion: Excursion):
    new_id = resolvers.excursion.new_excursion(excursion)
    return f'{{code: 201, id: {new_id}}}'