#!/usr/bin/python3
"""This modulecreate a generator that streams rows
   from an SQL database one by one - MySql.
"""

import mysql.connector
from mysql.connector import Error
import csv
import uuid


def connect_db():
    """Connect to the MySQL database via Unix socket and return the
       connection object.
    """
    connection = None
    try:
        connection = mysql.connector.connect(
            user='root',
            host='localhost',
            password='qw12ERty',
            unix_socket='/var/run/mysqld/mysqld.sock'

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
              user_id CHAR(36) PRIMARY KEY,
              name VARCHAR(255) NOT NULL,
              email VARCHAR(255) NOT NULL,
              age DECIMAL(3, 0) NOT NULL
            );
            """
            )
        if cursor.rowcount == 0:
            print("Table user_data created successfully")
    except Error as err:
        print(f'Error: {err}')


def insert_data(connection, data):
    """Inserts data in the database if it does not exist"""
    cursor = connection.cursor()
    try:
        with open(data, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                # Skip the header row
                if reader.line_num == 1:
                    continue
                # Generate a unique user_id for each row
                user_id = str(uuid.uuid4())
                name, email, age = row[0], row[1], row[2]
                # Insert the data into the database
                cursor.execute(
                    """
                    INSERT INTO user_data (user_id, name, email, age)
                    VALUES (%s, %s, %s, %s)
                    """,
                    (user_id, name, email, age)
                )
        connection.commit()
    except Error as err:
        print(f'Error: {err}')
        connection.rollback()
    finally:
        cursor.close()
