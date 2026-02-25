from flask import Flask, render_template, request
from db_config import get_db_connection

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/book", methods=["POST"])
def book():
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
        # Use str(e), NOT e.msg
        return f"Something went wrong: {str(e)}", 500
