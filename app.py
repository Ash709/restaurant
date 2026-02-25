from flask import Flask, render_template, request
from db_config import get_db_connection

app = Flask(__name__)

conn = get_db_connection()
conn.execute("""
CREATE TABLE IF NOT EXISTS bookings (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    phone TEXT,
    date TEXT,
    time TEXT,
    guests TEXT
)
""")
conn.commit()
conn.close()


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/book", methods=["POST"])
def book():
    name = request.form["name"]
    phone = request.form["phone"]
    date = request.form["date"]
    time = request.form["time"]
    guests = request.form["guests"]

    conn = get_db_connection()
    cursor = conn.cursor()

    query = """
    INSERT INTO bookings (name, phone, date, time, guests)
    VALUES (?, ?, ?, ?, ?)
    """

    cursor.execute(query, (name, phone, date, time, guests))
    conn.commit()

    cursor.close()
    conn.close()

    return render_template("thankyou.html")


if __name__ == "__main__":
    app.run(debug=True)
