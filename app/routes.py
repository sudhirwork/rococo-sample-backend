from flask import Blueprint, jsonify, request
from app.models import User
from app.database import db
import uuid
from flask_jwt_extended import create_access_token, jwt_required, create_refresh_token, get_jwt_identity, verify_jwt_in_request
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
import requests
from app.config import API_VERSION, FRONTEND_URL, EMAIL_SERVICE_URL

api_routes = Blueprint("api", __name__)

@api_routes.route("/users", methods=["GET"])
def get_users():
    sample_user = User(id="1", name="John Doe", email="john@example.com", password="secret")
    return jsonify(sample_user.dict())

# Signup API
@api_routes.route("/signup", methods=["POST"])
def signup():

    with db:

        data = request.json
        email = data.get("email")
        firstname = data.get("firstname")
        lastname = data.get("lastname")

        # password = data.get("password")  # Should be a temporary or generated password

        if not (firstname and lastname and email):
            return jsonify({"error": "Missing required fields"}), 400

        # Check if email exists
        existing_user = db.get_one("users", {"email": email})
        if existing_user:
            return jsonify({"error": "Email already registered"}), 400

        # Hash password
        # hashed_password = generate_password_hash(password)

        db.save("users", {
            "email": email,
            "firstname": firstname,
            "lastname": lastname,
        })

        get_user = db.get_one("users", {"email": email})
        if get_user:
            reset_token = str(uuid.uuid4())
            db.save('password_resets', {
                "user_id": get_user.get("id"),
                "token": reset_token
            })

            db.save('organizations', {
                "name": f"{firstname}'s organization",
                "user_id": get_user.get("id")
            })

        # return jsonify({"success": "User registered successfully", "token": reset_token}), 200

        # Send welcome email
        # reset_link = f"${FRONTEND_URL}/set-password?token={reset_token}"
        # email_payload = {
        #     "to": email,
        #     "subject": "Welcome to Our Service!",
        #     "message": f"Hello {firstname} {lastname},\n\nWelcome to our platform! Click here to set your password: {reset_link}"
        # }
        # requests.post(EMAIL_SERVICE_URL, json=email_payload)

        return jsonify({"message": "User registered successfully, check your email for a reset link"}), 201

# Signin API
@api_routes.route("/signin", methods=["POST"])
def signin():
    data = request.json
    email = data.get("email")
    password = data.get("password")

    if not (email and password):
        return jsonify({"error": "Missing email or password"}), 400
    
    with db:

        # Fetch user details
        user = db.get_one("users",{ "email": email })
        if not user or not check_password_hash(user["password"], password):
            return jsonify({"error": "Invalid email or password"}), 401

        # Generate JWT token
        access_token = create_access_token(identity=str(user["email"]))
        refresh_token = create_refresh_token(identity=str(user["email"]))
        return jsonify({"access_token": access_token, "refresh_token": refresh_token, "user": {
            "firstname": user["firstname"],
            "lastname": user["lastname"],
            "email": user["email"]
        }}), 200

# Password Reset Request API
@api_routes.route("/request-password-reset", methods=["POST"])
def request_password_reset():
    data = request.json
    email = data.get("email")

    if not email:
        return jsonify({"error": "Missing email"}), 400
    
    with db:

        user = db.get_one("users", { "email": email })
        if not user:
            return jsonify({"error": "User not found"}), 404

        # Generate a reset token
        reset_token = str(uuid.uuid4())
        db.execute_query(
            "INSERT INTO password_resets (user_id, token) VALUES (%s, %s) ON CONFLICT (user_id) DO UPDATE SET token = EXCLUDED.token",
            (user["id"], reset_token)
        )

        # Send reset email
        # reset_link = f"${FRONTEND_URL}/reset-password?token={reset_token}"
        # email_payload = {
        #     "to": email,
        #     "subject": "Password Reset Request",
        #     "message": f"Click here to reset your password: {reset_link}"
        # }
        # requests.post(EMAIL_SERVICE_URL, json=email_payload)

        return jsonify({"message": "Password reset link sent to your email"}), 200

# Reset Password API
@api_routes.route("/reset-password", methods=["POST"])
def reset_password():
    data = request.json
    token = data.get("token")
    password = data.get("password")

    if not (token and password):
        return jsonify({"error": "Missing token or new password"}), 400
    
    with db:

        # Validate token
        reset_entry = db.get_one("password_resets", { "token": token })
        if not reset_entry:
            return jsonify({"error": "Invalid or expired token"}), 400

        # Hash new password
        hashed_password = generate_password_hash(password)
        db.execute_query("UPDATE users SET password = %s WHERE id = %s", (hashed_password, reset_entry["user_id"]))

        # Delete the used token
        db.execute_query("DELETE FROM password_resets WHERE token = %s", (token,))

        return jsonify({"message": "Password reset successful"}), 200

# Refresh Token API
@api_routes.route('/refresh', methods=['POST'])
@jwt_required(refresh=True)
def refresh():
    current_user = get_jwt_identity()
    new_access_token = create_access_token(identity=current_user)
    return jsonify({"access_token": new_access_token})

# Verify Token API
@api_routes.route('/verify-token', methods=['POST'])
def verify_token():
    try:
        # Check if the token is present and valid
        verify_jwt_in_request()
        user_identity = get_jwt_identity()
        return jsonify({"valid": True, "user": user_identity})
    except Exception as e:
        return jsonify({"valid": False}), 401

# Dashboard API
@api_routes.route("/dashboard", methods=["GET"])
@jwt_required()
def dashboard():
    current_user = get_jwt_identity()
    print(current_user)
    return jsonify({"message": "Welcome to the dashboard!"}), 200

# Verion API
@api_routes.route("/version", methods=["GET"])
@jwt_required()
def get_version():

    with db:
        result = db.execute_query("SELECT version()")
        db_version = result[0]["version"] if result[0] else "Unknown"

        return jsonify({
            "api_version": API_VERSION,
            "database_version": db_version.split(" ")[1].replace(",", "")
        })