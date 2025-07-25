import mysql.connector

def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",       # replace with your MySQL username
        password="ASH@1234562003",   # replace with your MySQL password
        database="tastynuts"        # make sure this DB and 'bookings' table exist
    )
