#12 Convert the tables of marks attended by students in MySQL table in CSV data.

import mysql.connector
import csv

# --- Database connection setup ---
conn = mysql.connector.connect(
    host="localhost",
    user="root",       
    password="root",
    database="schooldb")
    
cur = conn.cursor()

# --- Create the marks table if not exists ---
cur.execute("""
CREATE TABLE IF NOT EXISTS marks (
    roll_no INT PRIMARY KEY,
    name VARCHAR(50),
    english INT,
    physics INT,
    chemistry INT,
    maths INT,
    computer INT
)
""")
conn.commit()


# --- Function to export table data to CSV ---
def export_to_csv():
    cur.execute("SELECT * FROM marks")
    rows = cur.fetchall()
    with open("student_marks.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Roll No", "Name", "English", "Physics", "Chemistry", "Maths", "Computer"])
        writer.writerows(rows)
    print("\n📁 Data exported successfully to 'student_marks.csv'!\n")


# --- Function to add or update student data ---
def add_or_update_student():
    roll = int(input("Enter Roll Number: "))
    name = input("Enter Name: ")
    eng = int(input("Enter English Marks: "))
    phy = int(input("Enter Physics Marks: "))
    chem = int(input("Enter Chemistry Marks: "))
    math = int(input("Enter Maths Marks: "))
    comp = int(input("Enter Computer Marks: "))

    # check if roll number already exists
    cur.execute("SELECT roll_no FROM marks WHERE roll_no = %s", (roll,))
    if cur.fetchone():
        cur.execute("""
            UPDATE marks SET name=%s, english=%s, physics=%s, chemistry=%s, maths=%s, computer=%s
            WHERE roll_no=%s
        """, (name, eng, phy, chem, math, comp, roll))
        print(" Student data updated successfully!")
    else:
        cur.execute("""
            INSERT INTO marks (roll_no, name, english, physics, chemistry, maths, computer)
            VALUES (%s,%s,%s,%s,%s,%s,%s)
        """, (roll, name, eng, phy, chem, math, comp))
        print(" New student added successfully!")

    conn.commit()


# --- Function to view all students ---
def view_students():
    cur.execute("SELECT * FROM marks")
    rows = cur.fetchall()
    if rows:
        print("\n--- Student Marks Table ---")
        for row in rows:
            print(row)
    else:
        print("\n(No records found.)")


# --- Main Menu ---
while True:
    print("\n====== SCHOOL MARKS MANAGEMENT ======")
    print("1. View Students")
    print("2. Add / Update Student Marks")
    print("3. Convert Table to CSV")
    print("4. Exit")

    choice = input("Enter choice (1-4): ")

    if choice == "1":
        view_students()
    elif choice == "2":
        add_or_update_student()
    elif choice == "3":
        export_to_csv()
    elif choice == "4":
        print("\nGoodbye ")
        break
    else:
        print("Invalid choice. Try again.")