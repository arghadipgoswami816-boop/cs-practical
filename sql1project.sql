CREATE TABLE IF NOT EXISTS student (
    admission INT PRIMARY KEY,
    name VARCHAR(50),
    class INT,
    sec VARCHAR(5)
);

ALTER TABLE student ADD marks INT DEFAULT 0;

INSERT INTO student (admission, name, class, sec, marks) VALUES (1, 'Riya', 12, 'A', 90);

INSERT INTO student (admission, name, class, sec, marks) VALUES (2, 'Aman', 12, 'A', 95);

INSERT INTO student (admission, name, class, sec, marks) VALUES (3, 'Kiran', 12, 'B', 76);

INSERT INTO student (admission, name, class, sec, marks) VALUES (4, 'Sahil', 12, 'B', 82);

UPDATE student SET marks = 90 WHERE name = 'Riya';

DELETE FROM student WHERE admission = 3;

SELECT * FROM student ORDER BY marks ASC;

SELECT sec,
MIN(marks),
MAX(marks),
SUM(marks),
COUNT(*),
AVG(marks)
FROM student
GROUP BY sec;
