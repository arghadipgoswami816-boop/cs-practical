CREATE DATABASE IF NOT EXISTS phonebook_db;

CREATE TABLE IF NOT EXISTS contacts (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    phone VARCHAR(15) NOT NULL UNIQUE
);

INSERT INTO contacts (name, phone) VALUES (%s, %s);

SELECT * FROM contacts WHERE phone = %s;

SELECT * FROM contacts WHERE name = %s;

SELECT * FROM contacts;

SELECT * FROM contacts WHERE name LIKE %s OR phone LIKE %s;

SELECT name, phone FROM contacts WHERE id = %s;

SELECT * FROM contacts WHERE phone = %s AND id != %s;

SELECT * FROM contacts WHERE name = %s AND id != %s;

UPDATE contacts SET name=%s, phone=%s WHERE id=%s;

DELETE FROM contacts WHERE id=%s;
