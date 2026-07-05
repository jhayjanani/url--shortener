from flask import Flask, render_template, request, redirect
import random
import string
import mysql.connector
from dotenv import load_dotenv
import os


load_dotenv()
app = Flask(__name__)

# MySQL Connection
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password=os.getenv("PASSWORD"),
    database="url_shortener"
)

cursor = connection.cursor()

# Home Page
@app.route("/", methods=["GET", "POST"])
def home():
    short_url = None

    if request.method == "POST":
        long_url = request.form["long_url"]

        # Generate random 6-character code
        short_url = ''.join(random.choices(string.ascii_letters + string.digits, k=6))

        # Save into MySQL
        query = """
        INSERT INTO url_mapping (long_url, short_url)
        VALUES (%s, %s)
        """

        values = (long_url, short_url)

        cursor.execute(query, values)
        connection.commit()

    return render_template("index.html", short_url=short_url)


# Redirect Short URL to Long URL
@app.route("/<short_url>")
def redirect_url(short_url):

    # Increase click count
    update_query = """
    UPDATE url_mapping
    SET clicks = clicks + 1
    WHERE short_url = %s
    """
    cursor.execute(update_query, (short_url,))
    connection.commit()

    # Get original URL
    select_query = """
    SELECT long_url
    FROM url_mapping
    WHERE short_url = %s
    """
    cursor.execute(select_query, (short_url,))
    result = cursor.fetchone()

    if result:
        return redirect(result[0])

    return "<h2>404 - Short URL Not Found</h2>"


if __name__ == "__main__":
    app.run(debug=True)