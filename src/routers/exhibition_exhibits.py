from fastapi import APIRouter
from sql_base.models import Exhibition_exhibits
import resolvers.exhibition_exhibits as res_exhibit

exhib_router = APIRouter()


@exhib_router.get('/')
def get_exhibition_exhibits():
    return f'Response: {{text: Страница со списком Выстовочных экспонатов}}'


@exhib_router.post('/create')
def new_exhibition_exhibits(exhibition_exhibits: Exhibition_exhibits):
    exhib_id = res_exhibit.new_exhibition_exhibits(exhibition_exhibits)
    return f'{{code: 201, id: {exhib_id}}}'


@exhib_router.get('/{exhibition_exhibits_id}')
def get_exhibition_exhibits(exhibition_exhibits_id: int):
    exhibition = res_exhibit(exhibition_exhibits_id)
    return f'Exhibition: {{title_exhibit:название экспоната, id: {exhibition_exhibits_id}}}'


@exhib_router.put('/exhibition_exhibits_id')
def update_exhibition_exhibits(exhibition_exhibits_id: int):
    return f'Update exhibition_exhibits {exhibition_exhibits_id}'


@exhib_router.delete('/exhibition_exhibits_id')
def delete_exhibition_exhibits_id(exhibition_exhibits_id: int):
    return f'delete exhibition_exhibits {exhibition_exhibits_id}'
