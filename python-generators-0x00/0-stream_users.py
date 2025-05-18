#!/usr/bin/python3
"""This module creates a generator that streams rows
   from Mysql database one by one.
"""

from mysql.connector import Error
seed = __import__('seed')


def stream_users():
    """Generator that streams rows from the user_data table one by one."""
    try:
        connection = seed.connect_to_prodev()
        if connection:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM user_data;")
            for row in cursor:
                yield row
            cursor.close()
            connection.close()
    except Error as err:
        print(f'Error: {err}')
