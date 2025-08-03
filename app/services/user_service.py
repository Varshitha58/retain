from app.db import get_db
from app.auth import hash_password, verify_password

conn, cursor = get_db()

def create_user(name, email, password):
    hashed = hash_password(password)
    cursor.execute("INSERT INTO users (name, email, password) VALUES (?, ?, ?)", (name, email, hashed))
    conn.commit()

def login_user(email, password):
    cursor.execute("SELECT id, password FROM users WHERE email = ?", (email,))
    row = cursor.fetchone()
    if row and verify_password(row[1], password):
        return (row[0],)
    return None

def fetch_all_users():
    cursor.execute("SELECT id, name, email FROM users")
    return cursor.fetchall()

def fetch_user_by_id(user_id):
    cursor.execute("SELECT id, name, email FROM users WHERE id = ?", (user_id,))
    return cursor.fetchone()

def create_user(name, email, password):
    cursor.execute("INSERT INTO users (name, email, password) VALUES (?, ?, ?)", (name, email, password))
    conn.commit()

def update_user(user_id, name, email):
    cursor.execute("UPDATE users SET name = ?, email = ? WHERE id = ?", (name, email, user_id))
    conn.commit()

def delete_user(user_id):
    cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))
    conn.commit()

def search_users_by_name(name):
    cursor.execute("SELECT id, name, email FROM users WHERE name LIKE ?", ('%' + name + '%',))
    return cursor.fetchall()

def login_user(email, password):
    cursor.execute("SELECT id FROM users WHERE email = ? AND password = ?", (email, password))
    return cursor.fetchone()
