from sql_base import base_worker
from sql_base import models


def new_post(post: models.Post) -> int:
    new_id = base_worker.insert_data("INSERT INTO post(post) "
                                    "VALUES(?) "
                                    "RETURNING post_id ",
                                     (post.post, ))
    return new_id