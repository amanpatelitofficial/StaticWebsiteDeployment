# init_db.py

import sqlite3
from werkzeug.security import generate_password_hash

# ---------------------------
# Step 1: Input username/password
# ---------------------------
username = 'alok'
password = 'alok123'

# ---------------------------
# Step 2: Hash password
# ---------------------------
hashed_password = generate_password_hash(password)

# ---------------------------
# Step 3: Connect to DB
# ---------------------------
conn = sqlite3.connect('database/users.db')
cursor = conn.cursor()

# ---------------------------
# Step 4: Create table
# ---------------------------
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL
)
''')

# ---------------------------
# Step 5: Insert or update user
# ---------------------------
cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
existing_user = cursor.fetchone()

if existing_user:
    cursor.execute("UPDATE users SET password = ? WHERE username = ?", (hashed_password, username))
    conn.commit()
    print(f"🔄 Password updated for user: {username}")
else:
    cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed_password))
    conn.commit()
    print(f"✅ New user created: {username}")

# ---------------------------
# Step 6: Show all users in the DB
# ---------------------------
print("\n📋 Current Users in DB:")
cursor.execute("SELECT id, username FROM users")
rows = cursor.fetchall()
for row in rows:
    print(f"🔹 ID: {row[0]} | Username: {row[1]}")

conn.close()

