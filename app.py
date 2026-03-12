```python
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Mock data for demo purposes
users = [
    {"id": 1, "name": "John Doe", "sleep_data": {"quality": 80, "duration": 7}},
    {"id": 2, "name": "Jane Doe", "sleep_data": {"quality": 70, "duration": 6}},
]

# API endpoint to get all users
@app.route("/users", methods=["GET"])
def get_users():
    return jsonify({"users": users})

# API endpoint to get user by ID
@app.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    user = next((user for user in users if user["id"] == user_id), None)
    if user:
        return jsonify({"user": user})
    return jsonify({"error": "User not found"}), 404

# API endpoint to create a new user
@app.route("/users", methods=["POST"])
def create_user():
    new_user = {
        "id": len(users) + 1,
        "name": request.json["name"],
        "sleep_data": {"quality": 0, "duration": 0},
    }
    users.append(new_user)
    return jsonify({"user": new_user}), 201

if __name__ == "__main__":
    app.run(debug=True)
```
