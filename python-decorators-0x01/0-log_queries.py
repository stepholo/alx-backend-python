#!/usr/bin/python3

import sqlite3
import functools
import logging
from datetime import datetime


# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')


def log_queries(func):
    """A decorator that logs the SQL query before executing it."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Assume the first argument is the query string
        query = args[0] if args else kwargs.get('query', 'Unknown query')
        logging.info(f"Executing query: {query}")
        return func(*args, **kwargs)
    return wrapper


@log_queries
def fetch_all_users(query):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    return results
