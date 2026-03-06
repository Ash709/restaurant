from flask import Flask, render_template, request
from db_config import get_db_connection
from mysql.connector import Error

app = Flask(__name__)

@app.route("/book", methods=["POST"])
def book():
    name = request.form["name"]
    phone = request.form["phone"]
    date = request.form["date"]
    time = request.form["time"]
    guests = request.form["guests"]

    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        query = """
        INSERT INTO bookings (name, phone, date, time, guests)
        VALUES (%s, %s, %s, %s, %s)
        """

        cursor.execute(query, (name, phone, date, time, guests))
        conn.commit()

        cursor.close()
        conn.close()

        print("Booking saved successfully")

    except Exception as e:
        print("Database connection failed:", e)

    
    return render_template("thankyou.html")
