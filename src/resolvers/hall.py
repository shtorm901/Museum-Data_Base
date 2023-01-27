from sql_base import base_worker
from sql_base import models


def new_hall(hall: models.Hall) -> int:
    hall_id = base_worker.insert_data("INSERT INTO hall(title_hall, floor)"
                                     "VALUES(?,?)"
                                     "RETURNING hall_id",
                                      (hall.title_hall, hall.floor))
    return hall_id
