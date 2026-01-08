import tkinter as tk
from tkinter import messagebox
import mysql.connector
import re
from datetime import datetime, date

# ------------ MYSQL CONNECTION ------------ #
db = mysql.connector.connect(
    host="localhost",
    user="root",          # change if needed
    password="root",      # change your MySQL password
    database="hotel_db"
)
cur = db.cursor()

# ------------ FUNCTIONS ------------ #

def validate_name(name):
    return re.fullmatch(r"[A-Za-z ]+", name)


def get_available_room(room_type):
    if room_type == "Single":
        rooms = range(1, 21)
    else:
        rooms = range(21, 41)

    cur.execute("SELECT room_no FROM reservations")
    booked = {r[0] for r in cur.fetchall()}

    for r in rooms:
        if r not in booked:
            return r
    return None


def reserve_room():
    name = entry_name.get().strip()
    aadhar = entry_aadhar.get().strip()
    room_type = room_var.get()
    adults = entry_adults.get()
    kids = entry_kids.get()
    checkin = entry_checkin.get()
    checkout = entry_checkout.get()

    # ---- Validations ---- #

    if not validate_name(name):
        messagebox.showerror("Error", "Name must contain only alphabets and spaces")
        return

    if not (aadhar.isdigit() and len(aadhar) == 12):
        messagebox.showerror("Error", "Aadhar must be a 12-digit number")
        return

    if not adults.isdigit() or not kids.isdigit():
        messagebox.showerror("Error", "Adults and Kids must be numbers")
        return

    adults = int(adults)
    kids = int(kids)

    try:
        checkin_date = datetime.strptime(checkin, "%Y-%m-%d").date()
        checkout_date = datetime.strptime(checkout, "%Y-%m-%d").date()
    except:
        messagebox.showerror("Error", "Date format should be YYYY-MM-DD")
        return

    if checkin_date < date.today():
        messagebox.showerror("Error", "Check-in date cannot be in the past")
        return

    if checkout_date <= checkin_date:
        messagebox.showerror("Error", "Checkout date must be after check-in")
        return

    if room_type == "Single":
        if adults > 1 or kids > 2:
            messagebox.showerror("Error", "Single room allows max 1 adult & 2 kids")
            return
        price = 3999
    else:
        if adults > 2 or kids > 3:
            messagebox.showerror("Error", "Double room allows max 2 adults & 3 kids")
            return
        price = 6999

    room_no = get_available_room(room_type)
    if not room_no:
        messagebox.showerror("Error", "No rooms available")
        return

    # ---- Insert into MySQL ---- #
    sql = """
    INSERT INTO reservations
    (room_no, name, aadhar, room_type, adults, kids, checkin, checkout, price)
    VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)
    """
    values = (room_no, name, aadhar, room_type, adults, kids,
              checkin, checkout, price)

    cur.execute(sql, values)
    db.commit()

    messagebox.showinfo(
        "Success",
        f"Room Reserved Successfully!\n\nRoom No: {room_no}\nPrice: ₹{price}"
    )

    clear_fields()


def clear_fields():
    entry_name.delete(0, tk.END)
    entry_aadhar.delete(0, tk.END)
    entry_adults.delete(0, tk.END)
    entry_kids.delete(0, tk.END)
    entry_checkin.delete(0, tk.END)
    entry_checkout.delete(0, tk.END)


# ------------ GUI ------------ #

root = tk.Tk()
root.title("Hotel Reservation System (MySQL)")
root.geometry("450x520")

tk.Label(root, text="Hotel Reservation System", font=("Arial", 16, "bold")).pack(pady=10)

frame = tk.Frame(root)
frame.pack(pady=10)

tk.Label(frame, text="Customer Name").grid(row=0, column=0, sticky="w")
entry_name = tk.Entry(frame)
entry_name.grid(row=0, column=1)

tk.Label(frame, text="Aadhar Number").grid(row=1, column=0, sticky="w")
entry_aadhar = tk.Entry(frame)
entry_aadhar.grid(row=1, column=1)

tk.Label(frame, text="Room Type").grid(row=2, column=0, sticky="w")
room_var = tk.StringVar(value="Single")
tk.OptionMenu(frame, room_var, "Single", "Double").grid(row=2, column=1)

tk.Label(frame, text="Adults").grid(row=3, column=0, sticky="w")
entry_adults = tk.Entry(frame)
entry_adults.grid(row=3, column=1)

tk.Label(frame, text="Kids").grid(row=4, column=0, sticky="w")
entry_kids = tk.Entry(frame)
entry_kids.grid(row=4, column=1)

tk.Label(frame, text="Check-in Date (YYYY-MM-DD)").grid(row=5, column=0, sticky="w")
entry_checkin = tk.Entry(frame)
entry_checkin.grid(row=5, column=1)

tk.Label(frame, text="Check-out Date (YYYY-MM-DD)").grid(row=6, column=0, sticky="w")
entry_checkout = tk.Entry(frame)
entry_checkout.grid(row=6, column=1)

tk.Button(root, text="Reserve Room", command=reserve_room,
          bg="green", fg="white", width=20).pack(pady=20)

root.mainloop()
