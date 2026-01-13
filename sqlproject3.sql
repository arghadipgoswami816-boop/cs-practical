CREATE DATABASE IF NOT EXISTS schooldb;
USE schooldb;
CREATE TABLE IF NOT EXISTS marks (
    rollno INT PRIMARY KEY,
    name VARCHAR(50),
    physics INT,
    chemistry INT,
    maths INT
);
DESCRIBE marks;
SELECT rollno FROM marks WHERE rollno=%s;
INSERT INTO marks VALUES (%s,%s,%s,%s,%s);
SELECT * FROM marks;
SELECT * FROM marks WHERE rollno=%s;
UPDATE marks SET physics=%s, chemistry=%s, maths=%s WHERE rollno=%s;
DELETE FROM marks WHERE rollno=%s;
