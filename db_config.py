def get_db_connection():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="ASH@1234562003",
            database="tastynuts",
            port=3306
        )
        print("Database Connected Successfully")
        return conn

    except mysql.connector.Error as err:
        print("MySQL Connection Error:", err)
        return None
