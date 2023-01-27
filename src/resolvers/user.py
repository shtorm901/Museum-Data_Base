from sql_base import base_worker
from sql_base import models


def check_login(user: models.User) -> int:
    query = "SELECT post FROM user WHERE login = ? AND password = ?"
    post_id = base_worker.insert_data(query, (user.login, user.password), many=False)
    return post_id