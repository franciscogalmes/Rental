import tkinter as tk
from tkinter import messagebox


def login():
    username = username_entry.get()
    password = password_entry.get()

    if username == "admin" and password == "password":
        messagebox.showinfo("Login Successful", "Welcome, Admin!")
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")


# Create the main window
root = tk.Tk()
root.title("Admin Login")

# Create and place widgets
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

# Start the Tkinter main loop
root.mainloop()
