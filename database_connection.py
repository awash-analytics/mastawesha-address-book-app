import sqlite3


class DatabaseConnection:

    def __init__(self, database_name='address_book.db'):
        self.database_name = database_name
        self.db = None

    def connect_database(self):
        try:
            self.db = sqlite3.connect(database=self.database_name)

            return self.db
        except sqlite3.Error as err:
            print('Err: ', err.message)

            return False

    def close_database(self):
        pass  # TODO complete close_database() function
