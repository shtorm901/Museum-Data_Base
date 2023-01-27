from fastapi import APIRouter
from sql_base.models import Information_about_the_excursion
import resolvers.information_about_the_excursion as res_excursion

info_router = APIRouter()


@info_router.get('/')
def get_info():
    return f'Response: {{text: Страница со списком экскурсий}}'


@info_router.post('/create')
def new_information(information_about_the_excursion: Information_about_the_excursion):
    info_id = res_excursion.new_information(information_about_the_excursion)
    return f'{{code: 210, id: {info_id}}}'


@info_router.get('{info_id}')
def get_information(info_id: int):
    information = res_excursion.get.information(info_id)
    return f'Information: {{number_of_people: число людей, id: {info_id}}}'


@info_router.put('/{info_id}')
def update_infromation(info_id: int):
    return f'Update information {info_id}'


@info_router.delete('/{info_id}')
def delete_information(info_id: int):
    return f'delete information {info_id}'
