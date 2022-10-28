import sqlite3

connection = sqlite3.connect('museum.db')
cur = connection.cursor()

with open("../sql/base.sql", 'r') as sql_file:
    scripts = sql_file.read()

for row in scripts.split(';'):
    try:
        cur.execute(row)
        connection.commit()
    except sqlite3.Error as error:
        print(error)