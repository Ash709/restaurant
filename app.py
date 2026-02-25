from flask import Flask, render_template, request, redirect
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


        query = """
INSERT INTO bookings (name, phone, date, time, guests)
VALUES (%s, %s, %s, %s, %s)
"""


        

        return render_template("thankyou.html")

    except Exception as e:
        return f"Something went wrong: {e}", 500
if __name__ == "__main__":
    app.run(debug=True)
