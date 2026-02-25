import mysql.connector

def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",       
        password="ASH@1234562003",   
        database="tastynuts"        
