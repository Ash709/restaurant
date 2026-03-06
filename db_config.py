import mysql.connector

def get_db_connection():
    return mysql.connector.connect(
        user="root",
        password="ASH@1234562003",
        database="tastynuts",
        unix_socket="/var/run/mysqld/mysqld.sock",
        auth_plugin='mysql_native_password'
    )
