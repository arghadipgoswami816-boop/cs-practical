#7. Create a binary file with roll no., name and marks, input a roll no. And update the marks.  
import pickle
import os

filename = "student.dat"

# ---------------- ADD STUDENT ----------------
def add_student():
    roll = int(input("Enter Roll Number: "))

    # Check if roll already exists
    if os.path.exists(filename):
        with open(filename, "rb") as f:
            try:
                while True:
                    s = pickle.load(f)
                    if isinstance(s, dict) and s.get("roll_no") == roll:
                        print("This roll number already exists.\n")
                        return
            except EOFError:
                pass

    name = input("Enter Name: ")
    marks = float(input("Enter Marks: "))

    with open(filename, "ab") as f:
        pickle.dump({"roll_no": roll, "name": name, "marks": marks}, f)

    print("Student added successfully.\n")


# ---------------- UPDATE MARKS ----------------
def update_marks():
    if not os.path.exists(filename):
        print("No records found.\n")
        return

    roll = int(input("Enter Roll Number to update: "))
    found = False
    students = []

    with open(filename, "rb") as f:
        try:
            while True:
                s = pickle.load(f)

                # Skip bad data
                if not isinstance(s, dict) or "roll_no" not in s:
                    students.append(s)
                    continue

                # Update marks
                if s["roll_no"] == roll:
                    print("Old Marks:", s["marks"])
                    s["marks"] = float(input("Enter New Marks: "))
                    print("Marks updated.\n")
                    found = True

                students.append(s)

        except EOFError:
            pass

    # If roll not found
    if not found:
        print("Student not found.\n")
        return

    # Write updated data
    with open(filename, "wb") as f:
        for s in students:
            pickle.dump(s, f)


# ---------------- DISPLAY ALL ----------------
def display_all():
    if not os.path.exists(filename):
        print("\nNo records found.\n")
        return

    empty = True

    with open(filename, "rb") as f:
        try:
            while True:
                s = pickle.load(f)

                if isinstance(s, dict) and "roll_no" in s:
                    empty = False
                    print(f"Roll: {s['roll_no']}, Name: {s['name']}, Marks: {s['marks']}")

        except EOFError:
            pass

    if empty:
        print("No records found.\n")
    else:
        print()


# ---------------- MAIN MENU ----------------
while True:
    print("1. Add Student")
    print("2. Update Marks")
    print("3. Display All")
    print("4. Exit")

    ch = input("Enter choice: ")

    if ch == "1":
        add_student()
    elif ch == "2":
        update_marks()
    elif ch == "3":
        display_all()
    elif ch == "4":
        print("Exiting...")
        break
    else:
        print("Invalid choice.\n")