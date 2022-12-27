from sql_base import base_worker
from sql_base import models


def new_worker(worker: models.Workers) -> int:
    new_id = base_worker.execute('INSERT INTO workers(surname, name) '
                                 'VALUES(?,?) '
                                 'RETURNING id',
                                 (worker.surname, worker.name))
    return new_id