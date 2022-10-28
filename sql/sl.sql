CREATE TABLE IF NOT EXISTS workers(
    workers_id INTEGER PRIMARY KEY AUTOINCREMENT,
    post_id INTEGER,
    name VARCHAR(20),
    surname VARCHAR(30),
    middle_name VARCHAR(30),
    phone_number INTEGER,
    FOREIGN KEY (post_id) REFERENCES post(post_id)
);

CREATE TABLE IF NOT EXISTS hall(
    hall_id INTEGER PRIMARY KEY AUTOINCREMENT,
    title_hall VARCHAR(30),
    floor VARCHAR(30)
);

CREATE TABLE IF NOT EXISTS excursion(
    excursion_id INTEGER PRIMARY KEY AUTOINCREMENT,
    floor INTEGER,
    exhibit_id INTEGER,
    workers_id INTEGER,
    info_id INTEGER,
    FOREIGN KEY (workers_id) REFERENCES workers(workers_id),
    FOREIGN KEY (exhibit_id) REFERENCES exhibition_exhibits(exhibit_id),
    FOREIGN KEY (info_id) REFERENCES information_about_the_excursion(info_id)
);

CREATE TABLE IF NOT EXISTS exhibition_exhibits(
    exhibit_id INTEGER PRIMARY KEY AUTOINCREMENT,
    hall_id INTEGER,
    title_exhibit VARCHAR(30),
    date_of_discovery DATE,
    FOREIGN KEY (hall_id) REFERENCES hall(hall_id)
);

CREATE TABLE IF NOT EXISTS post(
    post_id INTEGER PRIMARY KEY AUTOINCREMENT,
    post VARCHAR(30)
);

CREATE TABLE IF NOT EXISTS user(
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_name VARCHAR(30),
    user_password VARCHAR(30)
);

CREATE TABLE IF NOT EXISTS information_about_the_excursion(
    info_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    workers_id INTEGER,
    number_of_people INTEGER,
    FOREIGN KEY (user_id) REFERENCES user(user_id),
    FOREIGN KEY (workers_id) REFERENCES workers(workers_id)
);

INSERT INTO workers(name, surname, middle_name, phone_number, post_id)
VALUES ('Valerii', 'Baranov', 'Alekseevich', '+7(937)615-02-08', 5),
       ('Ivan', 'Semin', 'Aleksandrovich', '+7(999)015-92-01', 2),
       ('Andrey', 'Iliin', 'Nikolaevich', '+7(905)021-17-62', 6),
       ('Sergey', 'Shilov', 'Semenovich', '+7(996)510-07-05', 1),
       ('Matvey', 'Stoliarov', 'Dmitrievich', '+7(937)271-16-60', 3),
       ('Kirill', 'Korolev', 'Maksimovich', '+7(937)028-17-28', 4);

INSERT INTO hall(title_hall, floor)
VALUES ('Main_hall', '1'),
       ('Main_hall', '1'),
       ('Main_hall', '1'),
       ('Main_hall', '2'),
       ('Main_hall', '2'),
       ('Main_hall', '2');

INSERT INTO excursion(floor, exhibit_id, workers_id, info_id)
VALUES ('1', '1', '1', '1'),
       ('1', '2', '1', '2'),
       ('1', '3', '1', '3'),
       ('2', '4', '1', '4'),
       ('2', '5', '1', '5'),
       ('2', '6', '1', '6');

INSERT INTO exhibition_exhibits(hall_id, title_exhibit, date_of_discovery)
VALUES ('1', '', ''),
       ('2', '', ''),
       ('3', '', ''),
       ('4', '', ''),
       ('5', '', ''),
       ('6', '', '');