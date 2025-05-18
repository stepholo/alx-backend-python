#!/usr/bin/python3

from mysql.connector import Error
seed = __import__('seed').connect_to_prodev


def stream_users_in_batches(batch_size):
    """Generator that streams rows from the user_data table in batches."""

    connection = seed.connect_to_prodev()

    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM user_data")
            while True:
                rows = cursor.fetchmany(batch_size)
                if not rows:
                    break
                for row in rows:
                    yield row

        except Error as err:
            print(f'Error: {err}')
        finally:
            connection.close()


def batch_processing(batch_size):
    """that processes each batch to filter users over the age of 25`"""

    connection = seed.connect_to_prodev()

    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM user_data WHERE age > 25;")
            while True:
                rows = cursor.fetchmany(batch_size)
                if not rows:
                    break
                for row in rows:
                    yield row
            cursor.close()
        except Error as err:
            print(f'Error: {err}')
        finally:
            connection.close()
