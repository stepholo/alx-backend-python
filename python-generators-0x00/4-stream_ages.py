#!/usr/bin/python3
"""Use a generator to compute a memory-efficient aggregate function i.e
   average age for a large dataset
"""


def stream_user_ages():
    """A generator function that streams the ages of users from the database
       and computes the average age.
    """

    seed = __import__('seed').connect_to_prodev()

    connection = seed.connect_to_prodev()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT age FROM user_data")
    rows = cursor.fetchall()

    total_age = 0
    count = 0

    for row in rows:
        age = row['age']
        total_age += age
        count += 1
        yield age

    if count > 0:
        average_age = total_age / count
        print(f"Average age of users: {average_age}")
