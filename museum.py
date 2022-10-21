import sqlite3 as sql

connection = sql.connect('museum.db')
table_workers = """CREATE TABLE IF NOT EXISTS workers(
                Workers_id INTEGER PRIMARY KEY AUTOINCREMENT,
                Post_id INTEGER,
                surname VARCHAR(30),
                named VARCHAR(20),
                middle_name VARCHAR(30),
                telephone_number VARCHAR(30),
                UNIQUE (surname, named, middle_name, telephone_number),
                FOREIGN KEY (Post_id) REFERENCES Post(Post_id)

)"""
table_hall = """CREATE TABLE IF NOT EXISTS hall(
            Hall_id INTEGER PRIMARY KEY AUTOINCREMENT,
            Title_Hall VARCHAR(30),
            Floor INTEGER,
            Square INTEGER,
            UNIQUE (Title_Hall)

)"""

table_exhibition_exhibits = """CREATE TABLE IF NOT EXISTS exhibition_exhibits(
                            Exhibit_id INTEGER PRIMARY KEY AUTOINCREMENT,
                            Hall_id INTEGER,
                            Title_Exhibit VARCHAR(30),
                            Date_of_discovery DATA,
                            UNIQUE(Title_Exhibit),
                            FOREIGN KEY (Hall_id) REFERENCES Hall(Hall_id)

)"""

table_excursion = """CREATE TABLE IF NOT EXISTS excursion(
                    Excursion_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    Floor INTEGER,
                    Square VARCHAR(30),
                    Exhibit_id INTEGER,
                    Workers_id INTEGER,
                    Number_of_People INTEGER,
                    UNIQUE(Exhibit_id),
                    FOREIGN KEY (Exhibit_id) REFERENCES Exhibit(Exhibit_id),
                    FOREIGN KEY (Workers_id) REFERENCES Workers(Workers_id)
)"""

table_post = """CREATE TABLE IF NOT EXISTS post(
            Post_id INTEGER PRIMARY KEY AUTOINCREMENT,
            Post VARCHAR(30),
            UNIQUE(Post_id, Post)

)"""

table_User = """CREATE TABLE IF NOT EXISTS users(
            User_id INTEGER PRIMARY KEY AUTOINCREMENT,
            User_Name VARCHAR(30),
            UNIQUE(User_id, User_name)

)"""

with connection:
    try:
        cursor = connection.cursor()
        cursor.execute(table_workers)
        cursor.execute('INSERT INTO workers(Post_id, named, surname, middle_name, telephone_number) VALUES ("2","Aleksei", "Kamarov", "Ivanovich", "None")')
        connection.commit()
        cursor.execute('INSERT INTO workers(Post_id, named, surname, middle_name, telephone_number) VALUES ("1","Michail", "Morozov", "Alekseevich", "+7(999(617-19-02")')
        connection.commit()
        cursor.execute('INSERT INTO workers(Post_id, named, surname, middle_name, telephone_number) VALUES ("3", "Nikolay", "Semenov", "Aleksandrovich", "None")')
        connection.commit()
        cursor.execute('INSERT INTO workers(Post_id, named, surname, middle_name, telephone_number) VALUES ("3", "Anna", "Leonteva", "Andreevna", "+7(937)225-02-37")')
        connection.commit()
        cursor.execute(table_post)
        cursor.execute('INSERT INTO post(Post) VALUES ("Уборщик")')
        connection.commit()
        cursor.execute('INSERT INTO post(Post) VALUES ("Охранник")')
        connection.commit()
        cursor.execute('INSERT INTO post(Post) VALUES ("Экскурсовод")')
        connection.commit()
        cursor.execute('INSERT INTO post(Post) VALUES ("Заведующий музеем")')
        connection.commit()
        cursor.execute(table_hall)
        cursor.execute('INSERT INTO hall(Title_Hall, Floor, Square) VALUES ("бытовые предметы времен второй мировой войны", "1", "1")')
        connection.commit()
        cursor.execute('INSERT INTO hall(Title_Hall, Floor, Square) VALUES ("оружие времен второй мировой войны", "2", "3")')
        connection.commit()
        cursor.execute('INSERT INTO hall(Title_Hall, Floor, Square) VALUES ("одежды времен второй мировой войны", "3", "2")')
        connection.commit()
        cursor.execute(table_exhibition_exhibits)
        cursor.execute('INSERT INTO exhibition_exhibits(Hall_id, Title_Exhibit, Date_of_discovery) VALUES ("2", "Пулемет дегтярева", "2014")')
        connection.commit()
        cursor.execute('INSERT INTO exhibition_exhibits(Hall_id, Title_Exhibit, Date_of_discovery) VALUES ("1", "Открытка из госпиталя", "2012")')
        connection.commit()
        cursor.execute(table_excursion)
        cursor.execute('INSERT INTO excursion(Floor, Square, Exhibit_id, Workers_id, Number_of_People) VALUES ("1", "1", "2", "4", "50")')
        connection.commit()
        cursor.execute('INSERT INTO excursion(Floor, Square, Exhibit_id, Workers_id, Number_of_People) VALUES ("3", "2", "1", "3", "50")')
        connection.commit()
    except sql.Error as ex:
        print(ex)
        connection.rollback()