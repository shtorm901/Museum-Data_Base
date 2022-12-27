import os.path
import sqlite3

def Base_check(file_path: str) -> bool:
    return os.path.exists(file_path)

def Base_create(file_path: str, sql_file: str) -> None:
        connection = sqlite3.connect(file_path)
        cur = connection.cursor()

        with open(sql_file, 'r') as sql_file:
            scripts = sql_file.read()

        for row in scripts.split(';'):
            try:
                cur.execute(row)
                connection.commit()
            except sqlite3.Error as error:
                print(error)
                connection.rollback()