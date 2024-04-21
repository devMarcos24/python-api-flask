from flask import Flask, request
from src.controllers.task_controller import TaskController

app = Flask(__name__)
tasks = []

taskController = TaskController(request=request, list=tasks)


@app.route("/task", methods=["POST"])
def create_task():
    return taskController.create()


@app.route("/task/<int:id>", methods=["GET"])
def get_by_id(id):
    return taskController.find_by_id(id=id)


if __name__ == "__main__":
    app.run(debug=True, port=3000)
