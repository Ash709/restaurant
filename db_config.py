import os
import psycopg2

def get_db_connection():
    try:
        conn = psycopg2.connect(
            host=os.getenv("db_host"),
            database=os.getenv("db_name"),
            user=os.getenv("db_user"),
            password=os.getenv("db_password"),
            port=os.getenv("db_port")
        )
        return conn

    except Exception as e:
        print("Database error:", e)
        return None
