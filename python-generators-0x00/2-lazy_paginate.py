#!/usr/bin/python3

seed = __import__('seed')


def lazy_paginate(page_size):
    """A generator function lazypaginate(pagesize) that implements the
       paginate_users(page_size, offset) that will only fetch the next page
       when needed at an offset of 0
    """
    def paginate_users(page_size, offset):
        connection = seed.connect_to_prodev()
        cursor = connection.cursor(dictionary=True)
        cursor.execute(f"SELECT * FROM user_data LIMIT {page_size} OFFSET {offset}")
        rows = cursor.fetchall()
        connection.close()
        return rows

    offset = 0
    while True:
        rows = paginate_users(page_size, offset)
        if not rows:
            break
        for row in rows:
            yield row
        offset += page_size
