CREATE DATABASE IF NOT EXISTS snakegame;
USE snakegame;
CREATE TABLE IF NOT EXISTS users (
    username VARCHAR(50) PRIMARY KEY,
    password VARCHAR(100)
);
CREATE TABLE IF NOT EXISTS leaderboard (
    username VARCHAR(50),
    score INT
);
SELECT * FROM users WHERE username=%s;
INSERT INTO users VALUES (%s,%s);
SELECT * FROM users WHERE username=%s AND password=%s;
INSERT INTO leaderboard VALUES (%s,%s);
SELECT username, MAX(score) AS best
        FROM leaderboard
        GROUP BY username
        ORDER BY best DESC
        LIMIT 10;
