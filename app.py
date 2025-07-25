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

        

        return render_template("thankyou.html")

    except Exception as e:
        return f"Something went wrong: {e}", 500
import os

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
