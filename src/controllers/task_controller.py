from ..models.task import Task


class TaskController:
    def __init__(self, request, list=[]):
        self.request = request
        self.list = list

    def create(self):
        try:
            data = self.request.get_json()
            for item in self.list:
                if item["title"] == data["title"]:
                    return {"message": "title already exists", "status": 403}, 403

            new_task = Task(
                id=len(self.list) + 1,
                title=data["title"],
                description=data.get("description", ""),
            )

            self.list.append(new_task.to_dict())
            return self.list, 201
        except:
            return {"message": "i don't know what happened", "status": 400}, 400

    def find_by_id(self, id):
        for item in self.list:
            if item["id"] == id:
                return {"message": "here your task", "data": item, "status": 200}, 200

        return {"message": "task not found", "data": {}, "status": 404}, 404
