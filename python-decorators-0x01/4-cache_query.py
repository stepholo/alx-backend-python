#!/usr/bin/env python3

import time
import sqlite3
import functools


query_cache = {}


def with_db_connection(func):
    # ...existing code...
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        conn = sqlite3.connect('users.db')
        try:
            return func(conn, *args, **kwargs)
        finally:
            conn.close()
    return wrapper


def cache_query(func):
    """Decorator to cache query results based on the SQL query string and log cache usage time."""
    @functools.wraps(func)
    def wrapper(conn, *args, **kwargs):
        query = kwargs.get('query') if 'query' in kwargs else (args[0] if args else None)
        if query in query_cache:
            print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] Returning cached result for query: {query}")
            return query_cache[query]
        start = time.time()
        result = func(conn, *args, **kwargs)
        elapsed = time.time() - start
        print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] Query executed in {elapsed:.4f} seconds: {query}")
        query_cache[query] = result
        return result
    return wrapper


@with_db_connection
@cache_query
def fetch_users_with_cache(conn, query):
    # ...existing code...
    cursor = conn.cursor()
    cursor.execute(query)
    return cursor.fetchall()
