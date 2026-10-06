from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)

CORS(app)

# Temporary users
users = [
    {
        "username": "aravind",
        "email": "aravind@gmail.com",
        "password": "1234"
    }
]


@app.route("/")
def home():
    return "Flask Backend is Running!"


# LOGIN
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


# REGISTER
@app.route("/register", methods=["POST"])
def register():

    data = request.get_json()

    username = data.get("username")
    email = data.get("email")
    password = data.get("password")

    # Check required fields
    if not username or not email or not password:
        return jsonify({
            "success": False,
            "message": "All fields are required"
        }), 400

    # Check if username already exists
    for user in users:

        if user["username"] == username:
            return jsonify({
                "success": False,
                "message": "Username already exists"
            }), 409

        if user["email"] == email:
            return jsonify({
                "success": False,
                "message": "Email already registered"
            }), 409

    # Create new user
    new_user = {
        "username": username,
        "email": email,
        "password": password
    }

    users.append(new_user)

    return jsonify({
        "success": True,
        "message": "Registration successful"
    }), 201


if __name__ == "__main__":
    app.run(debug=True, port=5000)