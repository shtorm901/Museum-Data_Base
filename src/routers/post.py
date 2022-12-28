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



@post_router.get('/{post_id}')
def get_post(post_id: int):
    post = resolvers.get_post(post_id)
    return f'Post: {{post: название профессии, id:{post_id}}}'


@post_router.put('/{post_id}')
def update_post(post_id: int):
    return f'Update post {post_id}'


@post_router.delete('/{post_id}')
def delete_post(post_id :int):
    return f'delete post {post_id}'