# app/validators.py

import re

def is_valid_email(email):
    return re.match(r"^[\w\.-]+@[\w\.-]+\.\w+$", email)

def is_valid_password(password):
    return len(password) >= 6

def validate_user_data(data):
    if "name" not in data or not data["name"].strip():
        return False, "Name is required"
    if "email" not in data or not is_valid_email(data["email"]):
        return False, "Invalid email"
    if "password" not in data or not is_valid_password(data["password"]):
        return False, "Password must be at least 6 characters"
    return True, ""
