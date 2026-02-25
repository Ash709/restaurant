from flask import Flask, render_template, request, redirect
from db_config import get_db_connection

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/book", methods=["POST"])
def book():
     print("BOOK ROUTE HIT")
    try:
        name = request.form["name"]
        phone = request.form["phone"]
        date = request.form["date"]
        time = request.form["time"]
        guests = request.form["guests"]
       
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

        return render_template("thankyou.html")

    except Exception as e:
        return f"Something went wrong: {e}", 500
