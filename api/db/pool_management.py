from psycopg2 import pool
from contextlib import contextmanager
import os


connection_pool = pool.SimpleConnectionPool(
    0,
    20,
    dsn=os.getenv('DATABASE_URI')
)


@contextmanager
def get_curs():
    conn = connection_pool.getconn()
    try:
        with conn:
            yield conn.cursor()
    finally:
        connection_pool.putconn(conn=conn)