from psycopg2 import pool
from contextlib import contextmanager
from flask import current_app
import os

def create_db_pool():
    connection_pool = pool.SimpleConnectionPool(
        0,
        20,
        dsn=os.getenv('DATABASE_URI')
    )
    return connection_pool


@contextmanager
def get_curs():
    conn_pool = current_app.config.get('DB_POOL')
    conn = conn_pool.getconn()
    try:
        with conn:
            yield conn.cursor()
    finally:
        conn_pool.putconn(conn=conn)
