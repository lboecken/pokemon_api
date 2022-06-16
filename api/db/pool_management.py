from psycopg2 import pool
from contextlib import contextmanager
from flask import current_app
import os

def create_db_pool():
    connection_pool = pool.SimpleConnectionPool(
        0,
        20,
        dbname=os.getenv('DB_NAME'),
        password=os.getenv('DB_PASSWORD'),
        user=os.getenv('DB_USER'),
        host=os.getenv('DB_HOST'),
        # port=os.getenv('DB_PORT')
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
