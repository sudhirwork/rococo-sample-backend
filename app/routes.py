from flask import Blueprint, jsonify
from app.models import User

api_routes = Blueprint("api", __name__)

@api_routes.route("/users", methods=["GET"])
def get_users():
    sample_user = User(id="1", name="John Doe", email="john@example.com", password="secret")
    return jsonify(sample_user.dict())
