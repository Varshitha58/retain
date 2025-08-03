# app/routes.py

from flask import Blueprint, request, jsonify
from app.services.user_service import (
    fetch_all_users, fetch_user_by_id, create_user,
    update_user, delete_user, search_users_by_name,
    login_user
)

from app.validators import validate_user_data

user_bp = Blueprint("user_bp", __name__)

@user_bp.route("/users", methods=["GET"])
def get_users():
    users = fetch_all_users()
    return jsonify(users), 200

@user_bp.route("/user/<int:user_id>", methods=["GET"])
def get_user(user_id):
    user = fetch_user_by_id(user_id)
    if user:
        return jsonify(user), 200
    return jsonify({"error": "User not found"}), 404

@user_bp.route("/users", methods=["POST"])
def add_user():
    data = request.get_json()
    is_valid, msg = validate_user_data(data)
    if not is_valid:
        return jsonify({"error": msg}), 400
    create_user(data["name"], data["email"], data["password"])
    return jsonify({"message": "User created"}), 201

@user_bp.route("/user/<int:user_id>", methods=["PUT"])
def update_user_info(user_id):
    data = request.get_json()
    if "name" not in data or "email" not in data:
        return jsonify({"error": "Missing fields"}), 400
    update_user(user_id, data["name"], data["email"])
    return jsonify({"message": "User updated"}), 200

@user_bp.route("/user/<int:user_id>", methods=["DELETE"])
def delete_user_account(user_id):
    delete_user(user_id)
    return jsonify({"message": f"User {user_id} deleted"}), 200

@user_bp.route("/search", methods=["GET"])
def search_user():
    name = request.args.get("name")
    if not name:
        return jsonify({"error": "Missing name parameter"}), 400
    users = search_users_by_name(name)
    return jsonify(users), 200

@user_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    if "email" not in data or "password" not in data:
        return jsonify({"error": "Email and password required"}), 400
    user = login_user(data["email"], data["password"])
    if user:
        return jsonify({"status": "success", "user_id": user[0]}), 200
    return jsonify({"status": "failed"}), 401

@user_bp.route("/", methods=["GET"])
def health_check():
    return "User Management System", 200
