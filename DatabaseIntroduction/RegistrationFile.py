import tkinter as tk
import sqlite3
from tkinter import messagebox

def register():
    username = username_entry.get()
    password = password_entry.get()

    # Connect to the database
    conn = sqlite3.connect('user_database.db')
    cursor = conn.cursor()

    # Check if the username already exists
    cursor.execute("SELECT * FROM users WHERE username=?", (username,))
    existing_user = cursor.fetchone()

    if existing_user:
        messagebox.showerror("Registration Failed", "Username already exists.")
    else:
        # Insert the new user into the database
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        conn.commit()
        conn.close()
        messagebox.showinfo("Registration Successful", "Registration successful!")

# Create the registration window
root = tk.Tk()
root.title("User Registration")

frame = tk.Frame(root)
frame.pack(padx=20, pady=20)

username_label = tk.Label(frame, text="Username:")
username_label.grid(row=0, column=0, sticky="w")

username_entry = tk.Entry(frame)
username_entry.grid(row=0, column=1)

password_label = tk.Label(frame, text="Password:")
password_label.grid(row=1, column=0, sticky="w")

password_entry = tk.Entry(frame, show="*")
password_entry.grid(row=1, column=1)

register_button = tk.Button(frame, text="Register", command=register)
register_button.grid(row=2, columnspan=2)

root.mainloop()
