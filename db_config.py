import mysql.connector

def get_db_connection():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="ASH@1234562003",
            database="tastynuts",
            
        )
        return conn

    except mysql.connector.Error as err:
        print("MySQL Error:", err)
        return None
