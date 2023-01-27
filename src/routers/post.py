from fastapi import APIRouter
from sql_base.models import Post
import resolvers.post as res_post

post_router = APIRouter()


@post_router.get('/')
def get_post():
    return f'Response: {{text: Страница со списком должностей}}'

@post_router.post('/create')
def new_post(post: Post):
    new_id = res_post.new_post(post)
    return f'{{code: 201, id: {new_id}}}'


@post_router.get('/{post_id}')
def get_post(post_id: int):
    post = res_post.get_post(post_id)
    return f'Post: {{post: название профессии, id:{post_id}}}'


@post_router.put('/{post_id}')
def update_post(post_id: int):
    return f'Update post {post_id}'


@post_router.delete('/delete{post_id}')
def del_post(post: Post):
    del_id = res_post.del_post(post)
    return f'{{code: 201, id: {del_id}}}'