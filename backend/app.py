from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)

CORS(app)

# -------------------------
# Users
# -------------------------

users = [
    {
        "username": "aravind",
        "email": "aravind@gmail.com",
        "password": "1234"
    }
]


# -------------------------
# Dashboard
# -------------------------

@app.route("/dashboard", methods=["GET"])
def dashboard():

    return jsonify({
        "success": True,
        "message": "Welcome to the Dashboard",
        "options": [
            "Login",
            "Register"
        ]
    }), 200


# -------------------------
# Login
# -------------------------

@app.route("/login", methods=["POST"])
def login():

    data = request.get_json()

    username = data.get("username")
    password = data.get("password")

    for user in users:
        if user["username"] == username and user["password"] == password:

            return jsonify({
                "success": True,
                "message": "Login successful"
            }), 200

    return jsonify({
        "success": False,
        "message": "Invalid username or password"
    }), 401


# -------------------------
# Register
# -------------------------

@app.route("/register", methods=["POST"])
def register():

    data = request.get_json()

    username = data.get("username")
    email = data.get("email")
    password = data.get("password")

    if not username or not email or not password:

        return jsonify({
            "success": False,
            "message": "All fields are required"
        }), 400

    # Check duplicate username/email

    for user in users:

        if user["username"] == username:

            return jsonify({
                "success": False,
                "message": "Username already exists"
            }), 400

        if user["email"] == email:

            return jsonify({
                "success": False,
                "message": "Email already exists"
            }), 400

    # Add new user

    users.append({
        "username": username,
        "email": email,
        "password": password
    })

    return jsonify({
        "success": True,
        "message": "Registration successful"
    }), 201


# -------------------------
# Home
# -------------------------

@app.route("/")
def home():

    return "Flask Backend is Running!"


# -------------------------
# Run server
# -------------------------

if __name__ == "__main__":
    app.run(debug=True, port=5000)