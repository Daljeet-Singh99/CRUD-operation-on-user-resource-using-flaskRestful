# CRUD-operation-on-user-resource-using-flaskRestful


    Navigate to the project directory

    Start the MongoDB server on your machine.

    Activate the virtual environment

    use pip install -r Requirements.txt to install requirements

    Run the Flask application

The application should now be running on http://localhost:5000.
API Endpoints

    POST /users: Create a new user. Send a JSON payload with the user data (name, email, password) in the request body.
    GET /users: Get a list of all users.
    GET /users/<user_id>: Get a specific user by ID.
    PUT /users/<user_id>: Update a specific user by ID. Send a JSON payload with the updated user data in the request body.
    DELETE /users/<user_id>: Delete a specific user by ID.

Testing the API

You can test the API endpoints using a tool like Postman.

    Open Postman or any API testing tool.
    Send requests to the above-mentioned API endpoints (e.g., http://localhost:5000/users).
    For POST and PUT requests, provide the necessary JSON payload in the request body.
    Review the responses received from the server.
