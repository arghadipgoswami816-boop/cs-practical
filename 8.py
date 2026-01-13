"""8. Create a student table and insert data implement the following sql commands on the student table.
Alter table to add new attributes.
Update table to modify data
Order by to display data in ascending under.
Delete to remove tuple (s).
Group by and find the min, max, sum, count and average.
Admission, name, class, sec"""

import mysql.connector as sql

con = sql.connect(
    host="localhost",
    user="root",
    password="root123",
    database="school"
)
cur = con.cursor()

# 1) CREATE TABLE (if not exists)
cur.execute("""
CREATE TABLE IF NOT EXISTS student (
    admission INT PRIMARY KEY,
    name VARCHAR(50),
    class INT,
    sec VARCHAR(5)
)
""")
print("Table checked/created.")

# 2) CHECK IF marks column exists, if not → add it
cur.execute("SHOW COLUMNS FROM student LIKE 'marks'")
col = cur.fetchone()

if not col:
    cur.execute("ALTER TABLE student ADD marks INT DEFAULT 0")
    print("Marks column added.")
else:
    print("Marks column already exists.")

# 3) INSERT DATA ONLY IF TABLE IS EMPTY
cur.execute("SELECT COUNT(*) FROM student")
count = cur.fetchone()[0]

if count == 0:
    data = [
        (1, 'Riya', 12, 'A', 90),
        (2, 'Aman', 12, 'A', 95),
        (3, 'Kiran', 12, 'B', 76),
        (4, 'Sahil', 12, 'B', 82)
    ]
    cur.executemany(
        "INSERT INTO student (admission, name, class, sec, marks) VALUES (%s, %s, %s, %s, %s)",
        data
    )
    con.commit()
    print("Default data inserted.")
else:
    print("Data already exists, skipping insert.")

# 4) UPDATE marks
cur.execute("UPDATE student SET marks = 90 WHERE name = 'Riya'")
con.commit()

# 5) DELETE a student
cur.execute("DELETE FROM student WHERE admission = 3")
con.commit()

# 6) ORDER BY marks
print("\nStudents in ascending order of marks:")
print("(admission, name, class, sec, marks)")
cur.execute("SELECT * FROM student ORDER BY marks ASC")
for row in cur.fetchall():
    print(row)

# 7) GROUP BY section → min, max, sum, count, avg
print("\nSection-wise statistics:")
print("(section, min_marks, max_marks, sum_marks, count, avg_marks)")
cur.execute("""
SELECT sec,
MIN(marks),
MAX(marks),
SUM(marks),
COUNT(*),
AVG(marks)
FROM student
GROUP BY sec
""")

for row in cur.fetchall():
    print(row)

con.close()
