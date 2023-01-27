from sql_base import base_worker
from sql_base import models


def new_workers(workers: models.Workers) -> int:
    work_id = base_worker.insert_data("INSERT INTO workers(post_id, surname, name, middle_name, phone_number) "
                                     "VALUES(?,?,?,?,?) "
                                     "RETURNING workers_id",
                                     (workers.post_id, workers.surname, workers.name,
                                      workers.middle_name, workers.phone_number))
    return work_id