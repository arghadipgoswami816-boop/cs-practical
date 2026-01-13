CREATE TABLE IF NOT EXISTS users (username VARCHAR(50) PRIMARY KEY, salt VARCHAR(64), pwd_hash VARCHAR(64));
SELECT username FROM users WHERE username=%s;
INSERT INTO users (username, salt, pwd_hash) VALUES (%s,%s,%s);
SELECT salt, pwd_hash FROM users WHERE username=%s;
