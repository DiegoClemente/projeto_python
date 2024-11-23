# Task Management API

This is a simple Task Management API built using Flask. It allows users to create, retrieve, update, and delete tasks. Each task has a title, description, and completion status. The API provides the basic CRUD operations to manage tasks in a simple and efficient way.

## Features

- **Create Tasks**: Allows you to create new tasks.
- **Get Tasks**: Retrieves a list of all tasks.
- **Get Task by ID**: Retrieves a task by its unique ID.
- **Update Task**: Allows you to update the task's details.
- **Delete Task**: Allows you to delete a task by its ID.

## API Endpoints

### 1. Create Tasks (`POST /tasks`)

Create a new task or multiple tasks.

**Request Body**:
```json
{
  "title": "Task Title",
  "description": "Task Description",
  "completed": false
}
```

**Response**:
```json
{
  "message": "1 task(s) created successfully",
  "tasks": [
    {
      "id": 1,
      "title": "Task Title",
      "description": "Task Description",
      "completed": false
    }
  ]
}
```

### 2. Get All Tasks (`GET /tasks`)

Retrieve a list of all tasks.

**Response**:
```json
[
  {
    "id": 1,
    "title": "Task Title",
    "description": "Task Description",
    "completed": false
  }
]
```

### 3. Get Task by ID (`GET /tasks/<task_id>`)

Retrieve a single task by its ID.

**Response**:
```json
{
  "id": 1,
  "title": "Task Title",
  "description": "Task Description",
  "completed": false
}
```

If the task is not found, the response will be:
```json
{
  "error": "Task not found"
}
```

### 4. Update Task (`PUT /tasks/<task_id>`)

Update an existing task.

**Request Body**:
```json
{
  "title": "Updated Task Title",
  "description": "Updated Task Description",
  "completed": true
}
```

**Response**:
```json
{
  "id": 1,
  "title": "Updated Task Title",
  "description": "Updated Task Description",
  "completed": true
}
```

### 5. Delete Task (`DELETE /tasks/<task_id>`)

Delete a task by its ID.

**Response**:
```json
{
  "message": "Task deleted successfully"
}
```

## Setup

### Prerequisites

- Python 3.x
- Flask

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/task-management-api.git
   ```

2. Navigate to the project directory:
   ```bash
   cd task-management-api
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Running the Application

To run the application locally:

1. Start the Flask application:
   ```bash
   python app.py
   ```

2. The API will be available at `http://127.0.0.1:5000/`.

### Testing the API

You can test the API using tools like [Postman](https://www.postman.com/) or [Insomnia](https://insomnia.rest/).

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
