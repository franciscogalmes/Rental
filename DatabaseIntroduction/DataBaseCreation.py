import sqlite3

# Create a connection to the database (or create a new one if it doesn't exist)
conn = sqlite3.connect('user_database.db')

# Create a cursor object to execute SQL commands
cursor = conn.cursor()

# Create a table to store user information (if it doesn't exist)
cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                  id INTEGER PRIMARY KEY,
                  username TEXT,
                  password TEXT
                )''')

# Commit the changes and close the connection
conn.commit()
conn.close()