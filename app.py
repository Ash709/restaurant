from flask import Flask, request, render_template
import psycopg2
import os

app = Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect(
        host=os.environ.get("db_host"),
        database=os.environ.get("db_name"),
        user=os.environ.get("db_user"),
        password=os.environ.get("db_password"),
        port=os.environ.get("db_port")
    )
    return conn



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
