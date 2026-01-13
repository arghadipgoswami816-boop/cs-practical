#6. create a csv file by entering user id and password read and search the password for given user id program it.

import csv
import os

# Make sure file exists
if not os.path.exists("users.csv"):
    with open("users.csv", "w", newline="") as f:
        pass

def username_exists(uid):
    with open("users.csv", "r") as f:
        r = csv.reader(f)
        for row in r:
            if row and row[0] == uid:
                return True
    return False


def add_users():
    with open("users.csv", "a", newline="") as f:
        w = csv.writer(f)
        n = int(input("How many users to add? "))

        for i in range(n):
            while True:
                uid = input(f"Enter user id for user {i+1}: ").strip()

                if username_exists(uid):
                    print("Username already exists. Please type another.\n")
                else:
                    break

            pwd = input("Enter password: ").strip()
            w.writerow([uid, pwd])

        print(f"{n} users added successfully.\n")


def search_user():
    uid_search = input("Enter user ID to search: ").strip()
    found = False

    with open("users.csv", "r") as f:
        r = csv.reader(f)
        for row in r:
            if row and row[0] == uid_search:
                print(f"User Found → ID: {row[0]}, Password: {row[1]}\n")
                found = True
                break

    if not found:
        print("User not found.\n")


# MAIN LOOP
while True:
    print("1. Add Users")
    print("2. Search User")
    print("3. Exit")
    choice = input("Enter choice (1/2/3): ").strip()

    if choice == "1":
        add_users()
    elif choice == "2":
        search_user()
    elif choice == "3":
        print("Exiting program...")
        break
    else:
        print("Invalid choice! Try again.\n")
