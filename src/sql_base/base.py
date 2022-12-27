import os
import sqlite3

class BaseWorker:

    def set_base_path(self, base_path:str):
        self.base_path = base_path
    def Base_check(self) -> bool:
        return os.path.exists(self.base_path)

    def Base_create(self, sql_file: str) -> None:
            connection = sqlite3.connect(self.base_path)
            cur = connection.cursor()

            with open(sql_file, 'r') as file:
                scripts = file.read()
                try:
                    cur.executescript(scripts)
                    connection.commit()
                except sqlite3.Error as error:
                    print(error)
                finally:
                    connection.close()
