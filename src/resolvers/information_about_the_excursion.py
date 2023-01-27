from sql_base import base_worker
from sql_base import models


def new_information(information_about_the_excursion: models.Information_about_the_excursion) ->int:
    info_id = base_worker.insert_data("INSERT INTO information_about_the_excursion(info_id, user_id,"
                                         "workers_id, number_of_people)"
                                         "VALUES(?,?,?,?)"
                                         "RETURNING info_id",
                                         (information_about_the_excursion.info_id, information_about_the_excursion.user_id,
                                         information_about_the_excursion.workers_id,
                                          information_about_the_excursion.number_of_people))
    return info_id