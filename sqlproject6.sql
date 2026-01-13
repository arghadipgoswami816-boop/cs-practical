CREATE DATABASE IF NOT EXISTS datadb;
CREATE TABLE IF NOT EXISTS students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    roll_no INT,
    name VARCHAR(50),
    marks INT
);
INSERT INTO students (roll_no, name, marks) VALUES (%s, %s, %s);
