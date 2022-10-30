from fastapi import APIRouter

visitor_router = APIRouter()


@visitor_router.get('/')
def get_museum():
    return 'Museum Page'


@visitor_router.get('/{visitor/id}')
def get_museum(visitor_id: int):
    return f'Visitor {visitor_id}'


@visitor_router.put('/{visitor/id')
def update_visitor(visitor_id: int):
    return f'Update visitor {visitor_id}'


@visitor_router.delete('/{visitor/id}')
def delete_visitor(visitor_id: int):
    return f'Delete visitor {visitor_id}'
