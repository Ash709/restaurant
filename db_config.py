import mysql.connector

def get_db_connection():
    try:
        conn = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="ASH@1234562003",
            database="tastynuts",
            port=3306
        )
        return conn

    except mysql.connector.Error as err:
        print("MySQL Error:", err)
        return None
