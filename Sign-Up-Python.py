import sqlite3
import bcrypt

# Connect to database (or create it if it doesn't exist)
conn = sqlite3.connect('database.db')
cursor = conn.cursor()

# Create the table (run only once)
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    email TEXT UNIQUE NOT NULL,
    hashed_password TEXT NOT NULL
)
''')
conn.commit()

# Function to add a user
def add_user(username, email, password):
    # Hash the password
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    try:
        cursor.execute('''
        INSERT INTO users (username, email, hashed_password)
        VALUES (?, ?, ?)
        ''', (username, email, hashed_password))
        conn.commit()
        print("User added successfully!")
    except sqlite3.IntegrityError:
        print("Error: Username or email already exists.")

# Example usage
if __name__ == "__main__":
    username = input("Enter username: ")
    email = input("Enter email: ")
    password = input("Enter password: ")  # In a real app, ensure password strength
    add_user(username, email, password)

conn.close()