from fastapi import APIRouter
from sql_base.models import Excursion
import resolvers.excursion as res_excursion

exc_router = APIRouter()


@exc_router.get('/')
def get_excursion():
    return f'Response: {{text: Страница со списком экскурсий}}'


@exc_router.post('/create')
def new_excursion(excursion: Excursion):
    exc_id = res_excursion.new_excursion(excursion)
    return f'{{code: 201, id: {exc_id}}}'


@exc_router.get('/{excursion_id}')
def get_excursion(excursion_id: int):
    excursion = res_excursion.get_excursion(excursion_id)
    return f'Excursion: {{floor: номер этажа, exhibit_id: номер предмета, workers_id: номер работника id: {excursion}}}'


@exc_router.put('/{excursion_id}')
def update_excursion(excursion_id: int):
    return f'Update excursion {excursion_id}'


@exc_router.delete('/{excursion_id}')
def delete_excursion(excursion_id: int):
    return f'delete excursion {excursion_id}'
