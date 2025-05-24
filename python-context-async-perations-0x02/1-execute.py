import sqlite3


class ExecuteQuery:
    """Class to manage db connection and execution of queries."""
    def __init__(self, db_name, query, param=None):
        self.db_name = db_name
        self.query = query
        self.param = param if param else ()
        self.connection = None
        self.results = []

    def __enter__(self):
        """Establish a database connection."""
        self.connection = sqlite3.connect(self.db_name)
        if self.connection:
            print(f'connection to {self.db_name} established')
            return self.connection
        cursor = self.connection.cursor()
        cursor.execute(self.query, self.param)
        self.results = cursor.fetchall()
        return self.results

    def __exit__(self, exc_type, exc_value, traceback):
        """Close the database connection."""
        if self.connection:
            self.connection.close()
            print(f'connection to {self.db_name} closed')
        if exc_type is not None:
            print(f'An error occurred: {exc_value}')
