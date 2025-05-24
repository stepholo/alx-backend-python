#!/usr/bin/python3


from contextlib import contextmanager
import sqlite3


class DatabaseConnection:
    """Context to manage opening and closing a database connection."""
    def __init__(self, db_name='users.db'):
        self.db_name = db_name
        self.connection = None

    def __enter__(self):
        """Open the database connection."""
        self.connection = sqlite3.connect(self.db_name)
        if self.connection:
            print(f'Connected to database: {self.db_name}')
            return self.connection

    def __exit__(self, exc_type, exc_value, traceback):
        """close the database connection."""
        if self.connection:
            self.connection.close()
            self.connection = None
        if exc_type is not None:
            print(f'An error occurred: {exc_value}')


@contextmanager
def db_connection():
    with DatabaseConnection(db_name='users.db') as db_conn:
        cursor = db_conn.execute('SELECT * FROM users')
        for row in cursor:
            yield row