# Task Management API Documentation

This is a simple Task Management API built using Flask. It allows users to create, retrieve, update, and delete tasks. Each task has a title, description, and completion status.

## API Endpoints

### 1. Create Tasks (`POST /tasks`)

This endpoint allows users to create one or more tasks. The task data should be sent in JSON format.

#### Request Body:
```json
{
  "title": "Task Title",
  "description": "Task Description"
}
```

#### Response:
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

This endpoint retrieves a list of all tasks.

#### Response:
```json
[
  {
    "id": 1,
    "title": "Task Title",
    "description": "Task Description",
    "completed": false
  },
  {
    "id": 2,
    "title": "Another Task",
    "description": "Another task description",
    "completed": true
  }
]
```

Additionally, the response includes the total number of tasks:
```json
{
  "Total tasks": 2
}
```

### 3. Get Task by ID (`GET /tasks/<task_id>`)

This endpoint retrieves a single task by its ID.

#### Response:
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

This endpoint updates an existing task. The request body should include the updated task information.

#### Request Body:
```json
{
  "title": "Updated Task Title",
  "description": "Updated Task Description",
  "completed": true
}
```

#### Response:
```json
{
  "id": 1,
  "title": "Updated Task Title",
  "description": "Updated Task Description",
  "completed": true
}
```

If the task is not found, the response will be:
```json
{
  "error": "Task not found"
}
```

### 5. Delete Task (`DELETE /tasks/<task_id>`)

This endpoint deletes a task by its ID.

#### Response:
```json
{
  "message": "Task deleted successfully"
}
```

If the task is not found, the response will be:
```json
{
  "error": "Task not found"
}
```

## Running the Application

To run the application, ensure you have Python and Flask installed. Then, run the following command:

```bash
python app.py
```

The API will be available at `http://127.0.0.1:5000/`.

## Conclusion

This API provides basic task management functionality using simple HTTP methods. You can use it to manage tasks by interacting with the endpoints described above.
