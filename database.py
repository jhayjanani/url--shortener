import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="jhayjanani@1126",
    database="url_shortener"
)

cursor = connection.cursor()
if connection.is_connected():
    print("MySQL Connected Successfully!")