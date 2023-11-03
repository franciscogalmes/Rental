import tkinter as tk
import sqlite3
from tkinter import messagebox

def login():
    username = username_entry.get()
    password = password_entry.get()

    conn = sqlite3.connect('user_database.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
    user = cursor.fetchone()

    if user:
        messagebox.showinfo("Login Successful", "Welcome, " + username + "!")
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")

# Create the login window
root = tk.Tk()
root.title("User Login")

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

login_button = tk.Button(frame, text="Login", command=login)
login_button.grid(row=2, columnspan=2)

root.mainloop()
