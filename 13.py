#13) With reference to practical 6th, convert that csv file to MySQL database

import mysql.connector
import csv

DB_HOST = "localhost"
DB_USER = "root"
DB_PASS = "root"  #change if required
DB_NAME = "schooldb"

conn = mysql.connector.connect(
    host=DB_HOST,
    user=DB_USER,
    password=DB_PASS,
    database=DB_NAME
)
cursor = conn.cursor()

# --- Create table ---
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50),
    marks INT
)
""")

# --- Read CSV file ---
with open("students.csv", "r") as file:
    data = csv.reader(file)
    next(data)  # Skip header row if present

    for row in data:
        name, marks = row
        cursor.execute("INSERT INTO students (name, marks) VALUES (%s, %s)", (name, marks))

# --- Save and close ---
conn.commit()
conn.close()

print("✅ CSV file has been successfully imported into MySQL database!")