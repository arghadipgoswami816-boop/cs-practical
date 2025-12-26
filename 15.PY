#15) Create a python program to manage marks of the students of the school examination using mysql. 


import mysql.connector
from mysql.connector import Error
# ---------------- DB CONNECTION ----------------
try:
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root"
    )
    cur = db.cursor()
except Error as e:
    print("MySQL Connection Error:", e)
    exit()

# ---------------- DATABASE SETUP ----------------

cur.execute("CREATE DATABASE IF NOT EXISTS schooldb")
cur.execute("USE schooldb")

# ---------------- TABLE SETUP ----------------

cur.execute("""
CREATE TABLE IF NOT EXISTS marks (
    rollno INT PRIMARY KEY,
    name VARCHAR(50),
    physics INT,
    chemistry INT,
    maths INT
)
""")

db.commit()

# ---------------- AUTO-DETECT ROLL COLUMN ----------------

cur.execute("DESCRIBE marks")
columns = cur.fetchall()
ROLL_COL = columns[0][0]   # first column name dynamically

# ---------------- UTILITY ----------------

def student_exists(roll):
    query = f"SELECT {ROLL_COL} FROM marks WHERE {ROLL_COL}=%s"
    cur.execute(query, (roll,))
    return cur.fetchone() is not None

# ---------------- ADD ----------------

def add_student():
    try:
        r = int(input("Enter Roll No: "))
        if student_exists(r):
            print("Student already exists!\n")
            return

        n = input("Enter Name: ")
        p = int(input("Enter Physics Marks: "))
        c = int(input("Enter Chemistry Marks: "))
        m = int(input("Enter Maths Marks: "))

        cur.execute(
            f"INSERT INTO marks VALUES (%s,%s,%s,%s,%s)",
            (r, n, p, c, m)
        )
        db.commit()
        print("Student Added Successfully!\n")

    except ValueError:
        print("Invalid input.\n")

# ---------------- SHOW ----------------

def show_all():
    cur.execute("SELECT * FROM marks")
    data = cur.fetchall()

    if not data:
        print("No records found.\n")
        return

    # Get column names dynamically
    cur.execute("DESCRIBE marks")
    columns = cur.fetchall()
    column_names = [col[0] for col in columns]

    print("\n*************************** STUDENT MARKS TABLE ***************************")
    print(f"Database: schooldb  |  Table: marks  |  Records: {len(data)}")
    print("**************************************************************************")

    # Calculate column widths based on data
    col_widths = {}
    for col_name in column_names:
        col_widths[col_name] = len(col_name)  # Start with header length

    # Check data for maximum widths
    for student in data:
        for i, value in enumerate(student):
            col_name = column_names[i]
            value_str = str(value)
            col_widths[col_name] = max(col_widths[col_name], len(value_str))

    # Ensure minimum widths
    for col_name in column_names:
        if col_name.lower() == 'rollno':
            col_widths[col_name] = max(col_widths[col_name], 6)
        elif col_name.lower() == 'name':
            col_widths[col_name] = max(col_widths[col_name], 15)
        else:
            col_widths[col_name] = max(col_widths[col_name], 8)

    # Create table header
    header_line = ""
    for i, col_name in enumerate(column_names):
        header_line += f" {col_name.capitalize():<{col_widths[col_name]}} "
        if i < len(column_names) - 1:
            header_line += "|"

    # Create separator line
    separator_line = ""
    for i, col_name in enumerate(column_names):
        separator_line += "-" * (col_widths[col_name] + 2)
        if i < len(column_names) - 1:
            separator_line += "+"

    print(header_line)
    print(separator_line)

    # Display data rows
    for student in data:
        row_line = ""
        for i, value in enumerate(student):
            col_name = column_names[i]
            row_line += f" {str(value):<{col_widths[col_name]}} "
            if i < len(column_names) - 1:
                row_line += "|"
        print(row_line)

    print(separator_line)
    print(f"\n{len(data)} rows in set")
    print()

# ---------------- SEARCH ----------------

def search():
    try:
        r = int(input("Enter Roll No: "))
        if not student_exists(r):
            print("Student not found!\n")
            return

        cur.execute(f"SELECT * FROM marks WHERE {ROLL_COL}=%s", (r,))
        student = cur.fetchone()

        # Get column names dynamically
        cur.execute("DESCRIBE marks")
        columns = cur.fetchall()
        column_names = [col[0] for col in columns]

        print("\n************************* STUDENT DETAILS *************************")
        print(f"Database: schooldb  |  Table: marks  |  Roll No: {r}")
        print("******************************************************************")

        # Calculate column widths based on data
        col_widths = {}
        for col_name in column_names:
            col_widths[col_name] = len(col_name)  # Start with header length

        # Check data for maximum widths
        for i, value in enumerate(student):
            col_name = column_names[i]
            value_str = str(value)
            col_widths[col_name] = max(col_widths[col_name], len(value_str))

        # Ensure minimum widths
        for col_name in column_names:
            if col_name.lower() == 'rollno':
                col_widths[col_name] = max(col_widths[col_name], 6)
            elif col_name.lower() == 'name':
                col_widths[col_name] = max(col_widths[col_name], 15)
            else:
                col_widths[col_name] = max(col_widths[col_name], 8)

        # Create table header
        header_line = ""
        for i, col_name in enumerate(column_names):
            header_line += f" {col_name.capitalize():<{col_widths[col_name]}} "
            if i < len(column_names) - 1:
                header_line += "|"

        # Create separator line
        separator_line = ""
        for i, col_name in enumerate(column_names):
            separator_line += "-" * (col_widths[col_name] + 2)
            if i < len(column_names) - 1:
                separator_line += "+"

        print(header_line)
        print(separator_line)

        # Display student data
        row_line = ""
        for i, value in enumerate(student):
            col_name = column_names[i]
            row_line += f" {str(value):<{col_widths[col_name]}} "
            if i < len(column_names) - 1:
                row_line += "|"
        print(row_line)

        print(separator_line)
        print("\n1 row in set")
        print()

    except ValueError:
        print("Invalid input.\n")

# ---------------- UPDATE ----------------

def update_marks():
    try:
        r = int(input("Enter Roll No: "))
        if not student_exists(r):
            print("Student does not exist!\n")
            return

        p = int(input("Physics: "))
        c = int(input("Chemistry: "))
        m = int(input("Maths: "))

        cur.execute(
            f"UPDATE marks SET physics=%s, chemistry=%s, maths=%s WHERE {ROLL_COL}=%s",
            (p, c, m, r)
        )
        db.commit()
        print("Marks Updated!\n")

    except ValueError:
        print("Invalid input.\n")

# ---------------- DELETE ----------------

def delete_student():
    try:
        r = int(input("Enter Roll No: "))
        if not student_exists(r):
            print("Student does not exist!\n")
            return

        cur.execute(f"DELETE FROM marks WHERE {ROLL_COL}=%s", (r,))
        db.commit()
        print("Student Deleted!\n")

    except ValueError:
        print("Invalid input.\n")

# ---------------- MENU ----------------

while True:
    print("1. Add Student")
    print("2. Show All Students")
    print("3. Search Student")
    print("4. Update Student Marks")
    print("5. Delete Student")
    print("6. Exit")

    ch = input("Choice: ")

    if ch == '1':
        add_student()
    elif ch == '2':
        show_all()
    elif ch == '3':
        search()
    elif ch == '4':
        update_marks()
    elif ch == '5':
        delete_student()
    elif ch == '6':
        break
    else:
        print("Invalid choice\n")
# ---------------- CLEANUP ----------------


db.close()  

