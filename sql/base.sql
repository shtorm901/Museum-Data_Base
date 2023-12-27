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

INSERT INTO User(user_name, user_password)
VALUES('admin', 'pass')