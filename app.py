```python
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Mock data for demonstration purposes
users = [
    {"id": 1, "name": "John Doe", "email": "john@example.com"},
    {"id": 2, "name": "Jane Doe", "email": "jane@example.com"},
]

# Route to get all users
@app.route("/users", methods=["GET"])
def get_users():
    return jsonify(users)

# Route to get a user by ID
@app.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    user = next((user for user in users if user["id"] == user_id), None)
    if user is None:
        return jsonify({"error": "User not found"}), 404
    return jsonify(user)

# Route to create a new user
@app.route("/users", methods=["POST"])
def create_user():
    new_user = {
        "id": len(users) + 1,
        "name": request.json["name"],
        "email": request.json["email"],
    }
    users.append(new_user)
    return jsonify(new_user), 201

if __name__ == "__main__":
    app.run(debug=True)
```
