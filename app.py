from flask import Flask, jsonify, request
from models.task import Task

app = Flask(__name__)

tasks = {}
task_id_control = 1

@app.route("/tasks", methods=["POST"])
def create_task():
    global task_id_control

    tasks_data = request.get_json()

    if not isinstance(tasks_data, list):
        tasks_data = [tasks_data]

    created_tasks = []

    for task_data in tasks_data:
        task = Task(task_id_control, task_data["title"], task_data["description"])
        tasks[task_id_control] = task
        created_tasks.append(task.to_dict())
        task_id_control += 1


    return jsonify({
        "message": f"{len(created_tasks)} task(s) created successfully",
        "tasks": created_tasks
    }), 201


@app.route("/tasks", methods=["GET"])
def get_tasks():
    return jsonify([task.to_dict() for task in tasks.values()], {"Total tasks": len(tasks)}), 200

@app.route("/tasks/<int:task_id>", methods=["GET"])
def get_task(task_id):
    task = tasks.get(task_id)
    if task is None:
        return jsonify({"error": "Task not found"}), 404
    return jsonify(task.to_dict()), 200

@app.route("/tasks/<int:task_id>", methods=["PUT"])
def update_task(task_id):
    task = tasks.get(task_id)
    if task is None:
        return jsonify({"error": "Task not found"}), 404
    task_data = request.get_json()
    task.title = task_data["title"]
    task.description = task_data["description"]
    task.completed = task_data["completed"]
    return jsonify(task.to_dict()), 200

@app.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    task = tasks.pop(task_id, None)
    if task is None:
        return jsonify({"error": "Task not found"}), 404
    return jsonify({"message": "Task deleted successfully"}), 200


if __name__ == "__main__":
    app.run(debug=True)
