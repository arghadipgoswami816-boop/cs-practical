#14) With reference to practical 7th, convert that .dat file to MySQL database

import mysql.connector
import pickle

DB_HOST = "localhost"
DB_USER = "root"
DB_PASS = "root123"
DB_NAME = "datadb"

# First connect without database to create it if needed
temp_conn = mysql.connector.connect(
    host=DB_HOST,
    user=DB_USER,
    password=DB_PASS
)
temp_cur = temp_conn.cursor()
temp_cur.execute(f"CREATE DATABASE IF NOT EXISTS {DB_NAME}")
temp_conn.commit()
temp_conn.close()

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
    roll_no INT,
    name VARCHAR(50),
    marks INT
)
""")

# --- Read .dat file ---
with open("student.dat", "rb") as file:
    try:
        while True:
            student = pickle.load(file)
            if isinstance(student, dict) and "roll_no" in student:
                roll_no = student["roll_no"]
                name = student["name"]
                marks = student["marks"]
                cursor.execute("INSERT INTO students (roll_no, name, marks) VALUES (%s, %s, %s)", (roll_no, name, marks))
    except EOFError:
        pass  # End of file reached

# --- Save and close ---
conn.commit()
conn.close()

print(".dat file has been successfully imported into MySQL database!")
