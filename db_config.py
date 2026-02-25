import os
import psycopg2

def get_db_connection():
    conn = psycopg2.connect(os.environ.get("DATABASE_URL"))
    return conn
