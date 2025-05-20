#!/usr/bin/python3

import sqlite3
import functools
from datetime import datetime


def log_queries(func=None):
    """A decorator that logs the SQL query before executing it."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Assume the first argument is the query string
        query = kwargs.get('query') if 'query' in kwargs else (args[0] if args else None)
        timestamp = datetime.now().isoformat()
        print(f"[{timestamp}] Executing SQL query: {query}")
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
