import sqlite3
from database_connection import DatabaseConnection


class ManageUsers:
    """
    This class manages users to add user, show users, update and delete user.
    In the class constructor, i.e., __init__, a database connection is established.
    """

    def __init__(self):

        # connect to database
        self.db = DatabaseConnection()
        self.db_connect = self.db.connect_database()

        # create a Cursor() method from established database connection
        self.cur = self.db_connect.cursor()

    # CRUD operations, i.e., 'C' in CRUD stands for Create, 'R' for Read,
    # 'U' for Update, and 'D' for Delete.
    def create_user(self, username, first_name, last_name,
                    password, password_again):

        # Validation step: check if username is already taken
        check_username = self.validate_username(username)

        if check_username:
            print("""
            WARNING MESSAGE - The username exists. Please try again.
            """)

            return False
        else:
            # Validation step: password validation
            check_password = self.validate_password(password, password_again)

            if check_password:

                # Register the user
                try:
                    query_insert_user = """
                    INSERT INTO users(username, first_name, last_name, password)
                    VALUES(?, ?, ?, ?)
                    """

                    params = (username, first_name, last_name, password)

                    self.cur.execute(query_insert_user, params)
                    self.db_connect.commit()

                    return True
                except sqlite3.Error as err:
                    print('Err: ', err.message)

                    return False
            else:
                print("""
                Password mismatch. Please try again!
                """)

                return False

    def read_users(self):

        try:
            query_show_users = "SELECT * FROM users"

            self.cur.execute(query_show_users)
            data = self.cur.fetchall()

            print("""
            --- List of users for AddressBook App ---
            """)

            for row in list(data):  # NOTE The list() function forces print()
                                    # to print all records returned by fetchall().
                print(row)

            return True
        except sqlite3.Error as err:
            print('Err: ', err.message)

            return False

    def update_user(self, username):
        pass  # TODO complete update_user() function

    def delete_user(self, username):
        pass  # TODO complete delete_user() function

    def login(self, username, password):

        try:
            query_login_credentials = """
            SELECT * FROM users 
            WHERE username = ? AND password = ?
            """

            params = (username, password)
            self.cur.execute(query_login_credentials, params)
            data = self.cur.fetchall()  # NOTE sqlite3 returns a tuple, e.g., (1, 'test', 'qwe', 'qwe', 'test')

            if data:
                # store user credentials as a dictionary
                result = {'id': data[0][0],
                          'username': data[0][1],
                          'first_name': data[0][2],
                          'last_name': data[0][3]}

                return result
            else:
                print("""
                WARNING MESSAGE - Login failed. Please try again!
                """)

                return False
        except sqlite3.Error as err:
            print('Err: ', err.message)

            return False

    def validate_username(self, username):

        try:
            query_find_user = "SELECT * FROM users WHERE username = ?"

            params = (username,)
            self.cur.execute(query_find_user, params)
            data = self.cur.fetchone()

            if data:
                return True
            else:
                return False
        except sqlite3.Error as err:
            print('Err: ', err.message)

            return False

    def validate_password(self, password, password_again):
        # TODO Method validate_password might be static - read and understand
        if password != password_again:
            return False
        else:
            return True

