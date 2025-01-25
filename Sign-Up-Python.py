import sqlite3
import bcrypt # type: ignore

def create_users_table():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            email TEXT UNIQUE NOT NULL,
            hashed_password TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def create_user(username, email, password):
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO users (username, email, hashed_password) VALUES (?, ?, ?)", (username, email, hashed_password.decode('utf-8')))
        conn.commit()
        print(f"User {username} created successfully.")
    except sqlite3.IntegrityError as e:
        print(f"Error creating user {username}: {e}") #Print error message
    conn.close()

def verify_user(username_or_email, password):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute("SELECT hashed_password FROM users WHERE username = ? OR email = ?", (username_or_email, username_or_email))
    result = cursor.fetchone()
    conn.close()

    if result:
        hashed_password = result[0].encode('utf-8')
        return bcrypt.checkpw(password.encode('utf-8'), hashed_password)
    return False

# Example Usage
create_users_table()
create_user("testuser", "test@email.com", "P@$$wOrd")
create_user("anotheruser", "another@email.com", "anotherpassword")
create_user("testuser", "test2@email.com", "somepassword") #Will print username already exists

if verify_user("testuser", "P@$$wOrd"):
    print("Login successful (username)!")
else:
    print("Login failed (username).")

if verify_user("test@email.com", "P@$$wOrd"):
    print("Login successful (email)!")
else:
    print("Login failed (email).")

if verify_user("testuser", "wrongpassword"):
    print("Login successful!")
else:
    print("Login failed (wrong password).")

if verify_user("nonexistentuser", "anypassword"):
    print("Login successful!")
else:
    print("Login failed (user not found).")