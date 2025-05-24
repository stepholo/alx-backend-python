#!/usr/bin/env python3
"""Asynchronous database operations to fetch users and older users concurrently."""

import aiosqlite
import asyncio


async def async_fetch_users():
    """Asynchronously fetch users from the database."""
    async with aiosqlite.connect('users.db') as db:
        cursor = await db.execute("SELECT * FROM users")
        users = await cursor.fetchall()
        await cursor.close()
        return users


async def async_fetch_older_users():
    """Asynchronously fetch users older than 40 years."""
    async with aiosqlite.connect('users.db') as db:
        cursor = await db.execute("SELECT * FROM users WHERE age > 40")
        older_users = await cursor.fetchall()
        await cursor.close()
        return older_users


async def fetch_concurrently():
    """Fetch users and older users concurrently."""
    users_task = asyncio.create_task(async_fetch_users())
    older_users_task = asyncio.create_task(async_fetch_older_users())
    users, older_users = await asyncio.gather(users_task, older_users_task)
    return users, older_users


if __name__ == "__main__":
    asyncio.run(fetch_concurrently())
