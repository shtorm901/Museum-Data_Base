from fastapi import APIRouter
from sql_base import Post
import resolvers.post

post_router = APIRouter()


@post_router.get('/')
def get_post():
    return f'Response: {{text: Страница со списком должностей}}'

@post_router.post('/')
def new_post(post: Post):
    new_id = resolvers.post.new_post(post)
    return f'{{code: 201, id: {new_id}}}'
