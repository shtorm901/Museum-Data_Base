from fastapi import FastAPI
from sql_base import base_worker
from settings import Base
from routers.post import post_router
from routers.worker import work_router
from routers.hall import hall_router
from routers.excursion import exc_router
from routers.exhibition_exhibits import exhib_router
from routers.information_about_the_excursion import info_router
from routers.user import user_router


base_worker.set_base_path(Base)


if not base_worker.Base_check():
    base_worker.Base_create('../sql/base.sql')


app = FastAPI()

@app.get("/")
def main_page():
    return {'page': 'Connection is corect'}


app.include_router(post_router, prefix='/post')
app.include_router(work_router, prefix='/workers')
app.include_router(exc_router, prefix='/excursion')
app.include_router(hall_router, prefix='/hall')
app.include_router(exhib_router, prefix='/exhibition')
app.include_router(info_router, prefix='/info')
app.include_router(user_router, prefix='/user')