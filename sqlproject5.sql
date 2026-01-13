CREATE DATABASE IF NOT EXISTS marksdb;
CREATE TABLE IF NOT EXISTS marks (
    roll_no INT PRIMARY KEY,
    name VARCHAR(50),
    english INT,
    physics INT,
    chemistry INT,
    maths INT,
    computer INT
);
SELECT * FROM marks;
SELECT roll_no FROM marks WHERE roll_no = %s;
UPDATE marks SET name=%s, english=%s, physics=%s, chemistry=%s, maths=%s, computer=%s WHERE roll_no=%s;
INSERT INTO marks (roll_no, name, english, physics, chemistry, maths, computer) VALUES (%s,%s,%s,%s,%s,%s,%s);
SELECT * FROM marks;
