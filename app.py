from flask import Flask, render_template, request
from mysql.connector import connect, Error
from db_config import DB_CONFIG, SOCKET_PATH  # we'll define these in db_config.py

app = Flask(__name__)

def get_db_connection_safe():
    """Try TCP connection first, fallback to Unix socket if TCP fails."""
    try:
        return connect(
            host=DB_CONFIG["host"],
            user=DB_CONFIG["user"],
            password=DB_CONFIG["password"],
            database=DB_CONFIG["database"],
            port=DB_CONFIG.get("port", 3306)
        )
    except Error as e:
        if e.errno == 2003:  # Can't connect to MySQL server
            # fallback to Unix socket
            return connect(
                user=DB_CONFIG["user"],
                password=DB_CONFIG["password"],
                database=DB_CONFIG["database"],
                unix_socket=SOCKET_PATH
            )
        else:
            raise

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

        conn = get_db_connection_safe()
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

    except Error as e:
        return f"MySQL Error: {str(e)}", 500
    except Exception as e:
        return f"Unexpected Error: {str(e)}", 500

if __name__ == "__main__":
    app.run(debug=True)
