from flask import Flask, render_template, request
import mysql.connector
import time

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

    # Always show thank you page
    return render_template("thankyou.html")
    except mysql.connector.Error as err:
        return f"MySQL Error: {err}"


# Run Flask App
if __name__ == "__main__":
    app.run(debug=True)
