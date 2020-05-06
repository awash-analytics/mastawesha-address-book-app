import sqlite3
from database_connection import DatabaseConnection


class ManageContacts:
    """
    This class manages user's contacts to add contact, show contacts, search contact, etc.
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
    def create_contact(self, first_name, last_name, address,
                       phone, email, notes, username):

        try:
            query_insert_contact = """
            INSERT INTO contacts(first_name, last_name, address,
                                 phone, email, notes, username)
            VALUES (?, ?, ?, ?, ?, ?, ?)
            """

            params = (first_name, last_name, address,
                      phone, email, notes, username)

            self.cur.execute(query_insert_contact, params)
            self.db_connect.commit()

            return True
        except sqlite3.Error as err:
            print('Err: ', err.message)

            return False

    def read_contacts(self, username):

        try:
            query_show_contacts = """
            SELECT * FROM contacts
            WHERE username = ?
            """

            params = (username,)

            self.cur.execute(query_show_contacts, params)
            data = self.cur.fetchall()

            print("""
            --- List of your contacts stored in AddressBook App ---
            """)

            for row in list(data):  # NOTE The list() function forces print()
                                    # to print all records returned by fetchall().
                print(row)

            return True
        except sqlite3.Error as err:
            print('Err: ', err.message)

            return False

    def update_contact(self, username, first_name, phone):
        # NOTE first_name and phone makes unique operation
        # TODO complete update_contact() function
        pass

    def delete_contact(self, username, first_name, last_name):
        # TODO In create_contacts() function implement defensive code to not allow user insert
        # TODO a new contact with existing first_name and last_name
        pass

    def search_contact(self, username, first_name_start):
        try:
            query_search = """
            SELECT * FROM contacts 
            WHERE username = ? AND first_name LIKE ?
            """

            first_name_pattern = first_name_start + '%'
            params = (username, first_name_pattern)

            self.cur.execute(query_search, params)
            data = self.cur.fetchall()

            if data:
                print("""
                --- Your search result: ---
                """)

                for row in list(data):
                    print(row)

                return True
            else:
                print("No contact found!")

                return False
        except sqlite3.Error as err:
            print('Err: ', err.message)

            return False
