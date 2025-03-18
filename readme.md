# Lonely Bag Assignment

This project is a FastAPI application that provides endpoints for managing users. It includes functionalities to create, read, update, and delete users, as well as search for users by name.

## Endpoints

- `POST /`: Create a new user
- `GET /search`: Search for users by name
- `GET /{id}`: Get a user by ID
- `PUT /{id}`: Update a user by ID
- `DELETE /{id}`: Delete a user by ID

## Models

- `UserRequest`: Model for creating users
- `UserResponse`: Model for user responses
- `UserUpdateRequest`: Model for  updating users

## Setup and Installation

1. Clone the repository:
    ```bash
    git clone <repository-url>
    cd lonely_bag_assignment
    ```

2. Create and activate a virtual environment:

    - On macOS and Linux:
        ```bash
        python3 -m venv venv
        source venv/bin/activate
        ```

    - On Windows:
        ```bash
        python -m venv venv
        .\venv\Scripts\activate
        ```

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```


5. Run the FastAPI application:
    ```bash
    uvicorn main:app --reload
    ```

6. Open your browser and navigate to `http://127.0.0.1:8000/docs` to access the API documentation.

## Project Structure

- `endpoints/`: Contains the API endpoint definitions
- `models/`: Contains the Pydantic models for request and response validation
- `utils/` : Initialises the user array.