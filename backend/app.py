from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)

# Enable CORS
CORS(app)


USER = {
    "username": "aravind",
    "password": "1234"
}


@app.route("/login", methods=["POST"])
def login():

    data = request.get_json()

    username = data.get("username")
    password = data.get("password")

    if username == USER["username"] and password == USER["password"]:
        return jsonify({
            "success": True,
            "message": "Login successful"
        }), 200

    return jsonify({
        "success": False,
        "message": "Invalid username or password"
    }), 401


@app.route("/")
def home():
    return "Flask Backend is Running!"


if __name__ == "__main__":
    app.run(debug=True, port=5000)