#!/usr/bin/python3
"""This modulecreate a generator that streams rows
   from an SQL database one by one - MySql.
"""

import mysql.connector
from mysql.connector import Error


def connect_db():
    """Connect to the MySQL database via Unix socket and return the
       connection object.
    """
    connection = None
    try:
        connection = mysql.connector.connect(
            user='root',
            unix_socket='/var/run/mysqld/mysqld.sock'
            # password is not needed if using auth_socket
        )
    except Error as err:
        print(f'Error: {err}')

    return connection


def create_database(connection):
    """Creates the database ALX_prodev if it does not exist"""
    cursor = connection.cursor()
    try:
        cursor.execute("CREATE DATABASE IF NOT EXISTS ALX_prodev;")
    except Error as err:
        print(f'Error: {err}')


def connect_to_prodev():
    """Connect to the ALX_prodev database and return the connection object."""
    connection = None
    try:
        connection = connect_db()
        connection.database = 'ALX_prodev'
    except Error as err:
        print(f'Error: {err}')

    return connection


def create_table(connection):
    """ creates a table user_data if it does not exists with the required
        fields
    """
    cursor = connection.cursor()
    try:
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS user_data (
              user_id(Primary Key, UUID, Indexed),
              name (VARCHAR, NOT NULL),
              email (VARCHAR, NOT NULL),
              age (DECIMAL,NOT NULL)
            );
            """
            )
    except Error as err:
        print(f'Error: {err}')


def insert_data(connection, data):
    """Inserts data in the database if it does not exist"""
    cursor = connection.cursor()
    try:
        cursor.execute(
            """
            INSERT INTO user_data (user_id, name, email, age)
            VALUES (%s, %s, %s, %s);
            """,
            data
        )
        connection.commit()
    except Error as err:
        print(f'Error: {err}')
        connection.rollback()