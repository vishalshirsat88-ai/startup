```markdown
# DreamWeaver API

This is a simple Flask MVP for the DreamWeaver startup idea. The API provides endpoints for managing users and their sleep data.

## Run Instructions

1. Clone the repository: `git clone https://github.com/your-repo/dreamweaver.git`
2. Install dependencies: `pip install -r requirements.txt`
3. Run the API: `python app.py`
4. Access the API at: `http://localhost:5000`

## API Endpoints

* `GET /users`: Get all users
* `GET /users/<int:user_id>`: Get user by ID
* `POST /users`: Create a new user

## Example Usage

* Get all users: `curl http://localhost:5000/users`
* Get user by ID: `curl http://localhost:5000/users/1`
* Create a new user: `curl -X POST -H "Content-Type: application/json" -d '{"name": "New User"}' http://localhost:5000/users`
```