from flask import Flask, request, render_template
import psycopg2
import os

app = Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect(
        host=os.environ.get("DB_HOST"),
        database=os.environ.get("DB_NAME"),
        user=os.environ.get("DB_USER"),
        password=os.environ.get("DB_PASSWORD"),
        port=os.environ.get("DB_PORT")
    )
    return conn


# CREATE TABLE AUTOMATICALLY
def create_table():
    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS bookings (
        id SERIAL PRIMARY KEY,
        name VARCHAR(100),
        phone VARCHAR(20),
        date DATE,
        time TIME,
        guests INTEGER
    );
    """)

    conn.commit()
    cur.close()
    conn.close()


# Run table creation when app starts
create_table()


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/book', methods=['POST'])
def book():
    name = request.form['name']
    phone = request.form['phone']
    date = request.form['date']
    time = request.form['time']
    guests = request.form['guests']

    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO bookings (name, phone, date, time, guests) VALUES (%s,%s,%s,%s,%s)",
        (name, phone, date, time, guests)
    )

    conn.commit()
    cur.close()
    conn.close()

    return "Booking Successful!"


if __name__ == '__main__':
    app.run()
