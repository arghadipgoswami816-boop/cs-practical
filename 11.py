#11 Snake Game with SQL for storing score and leaderboard. 

import pygame
import random
import mysql.connector
import sys
import hashlib

# ---------------- DATABASE SETUP ----------------

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root"
)
cur = db.cursor()

cur.execute("CREATE DATABASE IF NOT EXISTS snakegame")
cur.execute("USE snakegame")

cur.execute("""
CREATE TABLE IF NOT EXISTS users (
    username VARCHAR(50) PRIMARY KEY,
    password VARCHAR(100)
)
""")

cur.execute("""
CREATE TABLE IF NOT EXISTS leaderboard (
    username VARCHAR(50),
    score INT
)
""")
db.commit()

# ---------------- SECURITY ----------------

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# ---------------- USER AUTH ----------------

def register():
    print("\n--- REGISTER ---")
    username = input("Choose username: ")
    password = hash_password(input("Choose password: "))

    cur.execute("SELECT * FROM users WHERE username=%s", (username,))
    if cur.fetchone():
        print("Username already exists.")
        return None

    cur.execute("INSERT INTO users VALUES (%s,%s)", (username, password))
    db.commit()
    print("Registration successful.")
    return username

def login():
    print("\n--- LOGIN ---")
    username = input("Username: ")
    password = hash_password(input("Password: "))

    cur.execute("SELECT * FROM users WHERE username=%s AND password=%s", (username, password))
    if cur.fetchone():
        print("Login successful.")
        return username
    else:
        print("Invalid credentials.")
        return None

# ---------------- SCORE HANDLING ----------------

def save_score(username, score):
    cur.execute("INSERT INTO leaderboard VALUES (%s,%s)", (username, score))
    db.commit()

def show_leaderboard():
    cur.execute("""
        SELECT username, MAX(score) AS best
        FROM leaderboard
        GROUP BY username
        ORDER BY best DESC
        LIMIT 10
    """)
    data = cur.fetchall()

    print("\nTOP LEADERBOARD")
    for i, row in enumerate(data, 1):
        print(f"{i}. {row[0]} : {row[1]}")

# ---------------- PYGAME SETUP ----------------

pygame.init()

WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game with Login System")

clock = pygame.time.Clock()
snake_block = 10
snake_speed = 15

font = pygame.font.SysFont(None, 35)

def message(msg, color):
    screen.blit(font.render(msg, True, color), [WIDTH / 6, HEIGHT / 3])

# ---------------- GAME LOOP ----------------

def gameLoop():
    while True:  # Controls replay inside pygame

        x = WIDTH // 2
        y = HEIGHT // 2
        x_change = 0
        y_change = 0

        snake = []
        length = 1

        foodx = random.randrange(0, WIDTH, 10)
        foody = random.randrange(0, HEIGHT, 10)

        score = 0
        game_over = False

        while not game_over:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        x_change, y_change = -10, 0
                    elif event.key == pygame.K_RIGHT:
                        x_change, y_change = 10, 0
                    elif event.key == pygame.K_UP:
                        x_change, y_change = 0, -10
                    elif event.key == pygame.K_DOWN:
                        x_change, y_change = 0, 10

            x += x_change
            y += y_change

            if x < 0 or x >= WIDTH or y < 0 or y >= HEIGHT:
                game_over = True

            screen.fill((0, 0, 0))
            pygame.draw.rect(screen, (0, 255, 0), [foodx, foody, 10, 10])

            snake.append([x, y])
            if len(snake) > length:
                del snake[0]

            for part in snake[:-1]:
                if part == [x, y]:
                    game_over = True

            for part in snake:
                pygame.draw.rect(screen, (255, 255, 255), [part[0], part[1], 10, 10])

            pygame.display.update()

            if x == foodx and y == foody:
                foodx = random.randrange(0, WIDTH, 10)
                foody = random.randrange(0, HEIGHT, 10)
                length += 1
                score += 10

            clock.tick(snake_speed)

        # -------- GAME OVER SCREEN --------
        screen.fill((0, 0, 0))
        message("Game Over! Press Y to Play Again or N to Exit", (255, 0, 0))
        pygame.display.update()

        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_y:
                        waiting = False  # Restart game
                    elif event.key == pygame.K_n:
                        return score  # Exit game and return score
                elif event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

# ---------------- MAIN PROGRAM ----------------

print("SNAKE GAME SYSTEM ")
print("1. Register")
print("2. Login")

choice = input("Choose (1/2): ")

player = None
if choice == "1":
    player = register()
elif choice == "2":
    player = login()

if player:
    play = input("\nPress Y to Play: ").lower()
    if play == "y":
        final_score = gameLoop()
        save_score(player, final_score)
        print(f"\n Your Score: {final_score}")
        show_leaderboard()

pygame.quit()
