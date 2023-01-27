from fastapi import APIRouter
from sql_base.models import User
from resolvers import user

user_router = APIRouter()


@user_router.get('/')
def not_login():
    return {"Message": "Login in system"}


@user_router.post('/login')
def check_login(user: User, ):
    post = user.check_login(user)
    if post:
        return {"code": 200, "message": "Login currect!", 'post': post}
    else:
        return {"code": 401, "message": "Login incorrect!", 'post': None}