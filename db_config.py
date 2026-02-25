import mysql.connector

def get_db_connection():
    return mysql.connector.connect(
        user="root",
        password="ASH@1234562003",
        database="tastynuts",
        auth_plugin='mysql_native_password',
        unix_socket=r"\\.\pipe\MySQL80"
    )
