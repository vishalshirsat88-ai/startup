```markdown
# DreamWeaver Flask MVP

This is a basic Flask MVP for the DreamWeaver startup idea. The application provides API endpoints for user management and sleep data tracking.

## Run Instructions

1. Clone the repository: `git clone https://github.com/username/dreamweaver-flask-mvp.git`
2. Install dependencies: `pip install -r requirements.txt`
3. Run the application: `python app.py`
4. Access the API endpoints using a tool like `curl` or a REST client.

## API Endpoints

* `GET /users`: Get all users
* `GET /users/<int:user_id>`: Get user by ID
* `POST /users/<int:user_id>/sleep`: Update user sleep data

## Example Use Cases

* Get all users: `curl http://localhost:5000/users`
* Get user by ID: `curl http://localhost:5000/users/1`
* Update user sleep data: `curl -X POST -H "Content-Type: application/json" -d '{"sleep_data": ["2022-01-01", "2022-01-02"]}' http://localhost:5000/users/1/sleep`
```

Please note that this is a very basic implementation and you should consider security, authentication, and authorization for a production-ready application.