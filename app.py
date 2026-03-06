from flask import Flask, render_template, request
import mysql.connector
import time

app = Flask(__name__)

# Database connection function
def get_db_connection():
    try:
        conn = mysql.connector.connect(
        host="127.0.0.1",
        port=3306,
        user="root",
        password="ASH@1234562003",
        database="tastynuts",
        auth_plugin='mysql_native_password',
        connection_timeout=5
)
        )
        return conn
    except mysql.connector.Error as err:
        print("MySQL Connection Error:", err)
        return None


# Home Page
@app.route("/")
def home():
    return render_template("index.html")


@app.route("/book", methods=["POST"])
def book():
    name = request.form["name"]
    phone = request.form["phone"]
    date = request.form["date"]
    time_slot = request.form["time"]
    guests = request.form["guests"]

    conn = get_db_connection()
    if conn is None:
        return "Database connection failed. Please try again later."

    try:
        with conn.cursor() as cursor:
            query = """
            INSERT INTO bookings (name, phone, date, time, guests)
            VALUES (%s, %s, %s, %s, %s)
            """
            cursor.execute(query, (name, phone, date, time_slot, guests))
            conn.commit()
    except mysql.connector.Error as err:
        return f"MySQL Error: {err}"
    finally:
        if conn:
            conn.close()

    return render_template("thankyou.html")
