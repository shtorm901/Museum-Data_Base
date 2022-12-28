from sql_base import base_worker
from sql_base import models


def new_exhibition_exhibits(exhibition_exhibits: models.Exhibition_exhibits) -> int:
    new_id = base_worker.insert_data("INSERT INTO exhibition_exhibits(hall_id, title_exhibit, date_of_discovery)"
                                      "VALUES(?,?,?)"
                                      "RETURNING exhibit_id",
                                      (exhibition_exhibits.hall_id, exhibition_exhibits.title_exhibit,
                                       exhibition_exhibits.date_of_discovery))
    return new_id