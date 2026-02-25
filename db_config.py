import mysql.connector

def get_db_connection():
    return mysql.connector.connect(
        host="127.0.0.1",        # Use 127.0.0.1 on Windows
        user="root",
        password="ASH@1234562003",
        database="tastynuts"
    )
