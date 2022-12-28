from sql_base import base_worker
from sql_base import models

def new_excursion(excursion: models.Excursion) -> int:
    new_id = base_worker.insert_data("INSERT INTO excursion(floor, exhibit_id, workers_id, info_id)"
                                     "VALUES(?,?,?,?)"
                                     "RETURNING excursion_id",
                                     (excursion.floor, excursion.exhibit_id,
                                      excursion.workers_id, excursion.info_id))
    return new_id