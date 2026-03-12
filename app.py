**Flask MVP for DreamWeaver**

Below are the requested files for a basic Flask MVP for the DreamWeaver startup idea:

```python
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Mock data for demonstration purposes
users = [
    {"id": 1, "name": "John Doe", "sleep_data": []},
    {"id": 2, "name": "Jane Doe", "sleep_data": []}
]

# API endpoint to get all users
@app.route("/users", methods=["GET"])
def get_users():
    return jsonify(users)

# API endpoint to get user by ID
@app.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    user = next((user for user in users if user["id"] == user_id), None)
    if user is None:
        return jsonify({"error": "User not found"}), 404
    return jsonify(user)

# API endpoint to update user sleep data
@app.route("/users/<int:user_id>/sleep", methods=["POST"])
def update_sleep_data(user_id):
    user = next((user for user in users if user["id"] == user_id), None)
    if user is None:
        return jsonify({"error": "User not found"}), 404
    user["sleep_data"] = request.json["sleep_data"]
    return jsonify(user)

if __name__ == "__main__":
    app.run(debug=True)
```
