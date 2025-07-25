from flask import Flask, render_template, request, redirect
from db_config import get_db_connection

app = Flask(__name__)

# Homepage route
@app.route("/")
def home():
    return render_template("index.html")

# Booking form submission route
@app.route("/book", methods=["POST"])
def book():
    name = request.form["name"]
    phone = request.form["phone"]
    date = request.form["date"]
    time = request.form["time"]
    guests = request.form["guests"]

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO bookings (name, phone, date, time, guests) VALUES (%s, %s, %s, %s, %s)",
        (name, phone, date, time, guests)
    )
    conn.commit()
    cursor.close()
    conn.close()

    # Redirect to thank-you page
    return render_template("thankyou.html")

if __name__ == "__main__":
    app.run(debug=True)
