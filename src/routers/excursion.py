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

@exc_router.get('/{stud_id}')
def get_excursion(excursion_id: int):
    excursion = resolvers.get_excursion(excursion_id)
    return f'Excursion: {{floor: номер этажа, exhibit_id: номер предмета, workers_id: номер работника id: {excursion_id}}}'


@exc_router.put('/{stud_id}')
def update_excursion(excursion_id: int):
    return f'Update excursion {excursion_id}'


@exc_router.delete('/{stud_id}')
def delete_excursion(excursion_id: int):
    return f'delete excursion {excursion_id}'
