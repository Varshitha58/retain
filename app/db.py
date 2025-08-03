# app/db.py

import sqlite3

def get_db():
    conn = sqlite3.connect("users.db", check_same_thread=False)
    cursor = conn.cursor()
    return conn, cursor
