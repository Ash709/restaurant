from flask import Flask, render_template, request
import mysql.connector

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
            auth_plugin='mysql_native_password'
        )
        return conn
    except Exception as e:
        print("MySQL Connection Failed:", e)
        return None


# Home Page
@app.route('/')
def home():
    return render_template("index.html")


# Booking Route
@app.route('/book', methods=['POST'])
def book_table():
    
    name = request.form['name']
    phone = request.form['phone']
    date = request.form['date']
    time = request.form['time']
    guests = request.form['guests']

    conn = get_db_connection()

    # If database works
    if conn:
        try:
            cursor = conn.cursor()

            query = """
            INSERT INTO bookings (name, phone, date, time, guests)
            VALUES (%s, %s, %s, %s, %s)
            """

            cursor.execute(query, (name, phone, date, time, guests))
            conn.commit()

            cursor.close()
            conn.close()

            print("Booking saved to MySQL")

        except Exception as e:
            print("Database Insert Failed:", e)

    # If database fails
    else:
        print("Database not available. Booking received but not stored.")
        print("Booking Details:")
        print(name, phone, date, time, guests)

    return render_template("thankyou.html")


if __name__ == "__main__":
    app.run(debug=True)
