from sql_base import base_worker
from sql_base import models


def new_post(post: models.Post) -> int:
    new_id = base_worker.insert_data("INSERT INTO post(post) "
                                    "VALUES(?) "
                                    "RETURNING post_id ",
                                     (post.post, ))
    return new_id
def del_post(post_id: int) -> dict:
    del_id = base_worker.execute(query='DELETE FROM post WHERE post_id =?',
                               args=(post_id, ))
    return del_id