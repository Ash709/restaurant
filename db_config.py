import mysql.connector

def get_db_connection():
    try:
        conn = mysql.connector.connect(
            host="mysql.railway.internal",
            port=3306,
            user="root",
            password="ckzQadVYiVGWFNlKpPRiXrzrVDqPOLDM",
            database="railway"
        )
        return conn
    except mysql.connector.Error as err:
        print("Database Error:", err)
        return None
