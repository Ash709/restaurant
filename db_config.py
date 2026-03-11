import mysql.connector
import os

def get_db_connection():
    try:
        conn = mysql.connector.connect(
            host=os.getenv("DB_HOST", "centerbeam.proxy.rlwy.net"),
            port=int(os.getenv("DB_PORT", 16458)),
            user=os.getenv("DB_USER", "railway"),
            password=os.getenv("DB_PASSWORD", "ckzQadVYiVGWFNlKpPRiXrzrVDqPOLDM"),
            database=os.getenv("DB_NAME", "railway")
        )
        return conn

    except mysql.connector.Error as err:
        print("MySQL Error:", err)
        return None
