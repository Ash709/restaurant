from flask import Flask, render_template, request
from db_config import get_db_connection

app = Flask(__name__)


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
        cursor = conn.cursor()

        query = """
        INSERT INTO bookings (name, phone, date, time, guests)
        VALUES (%s, %s, %s, %s, %s)
        """

        cursor.execute(query, (name, phone, date, time_slot, guests))
        conn.commit()

        cursor.close()
        conn.close()

        return render_template("thankyou.html")

    except Exception as err:
        return f"MySQL Error: {err}"


import os

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
    
