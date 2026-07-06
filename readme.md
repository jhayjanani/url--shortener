🔗 URL Shortener

A simple URL Shortener web application built using Python, Flask, and MySQL. This project converts long URLs into short URLs and redirects users to the original website. It also tracks how many times each short URL has been accessed.

🚀 Features

- Convert long URLs into short URLs
- Redirect users to the original website
- Prevent duplicate URLs
- Track click count
- Store URL data in MySQL
- Simple and responsive user interface

🛠️ Technologies Used

- Python
- Flask
- MySQL
- HTML
- CSS
- SHA-256
- Base64
- python-dotenv

📂 Database

Database Name: "url_shortener"

Table Name: "url_mapping"

Column| Description
id| Unique ID
long_url| Original URL
short_url| Generated short URL
clicks| Number of times the short URL was opened
created_at| Date and time the URL was created

📌 Project Workflow

1. User enters a long URL.
2. Flask receives the request.
3. Python checks whether the URL already exists.
4. If it exists, the existing short URL is returned.
5. Otherwise, a new short URL is generated using SHA-256 and Base64.
6. The URL is stored in the MySQL database.
7. The short URL is displayed.
8. When the short URL is opened, the click count is updated and the user is redirected to the original URL.

▶️ How to Run

1. Clone the repository.
2. Create and activate a virtual environment.
3. Install the required packages:
   - Flask
   - mysql-connector-python
   - python-dotenv
4. Create the MySQL database and table.
5. Add your MySQL password to the ".env" file.
6. Run:

python app.py

7. Open your browser and visit:

http://127.0.0.1:5000/

📸 Output

- Generate a short URL from a long URL.
- Redirect to the original website.
- Track the number of clicks for each short URL.


