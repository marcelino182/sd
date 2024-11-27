from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from flask_cors import CORS

app = Flask(__name__)
api = Api(app)
CORS(app)

#  dicionario
tasks = {}
task_id_counter = 1

class Task(Resource):
    def get(self, task_id=None):
        # Retorna uma tarefa específica ou todas as tarefas.
        if task_id:
            task = tasks.get(task_id)
            if not task:
                return {"message": "Task not found"}, 404
            return task, 200
        return tasks, 200

    def post(self):
        # Cria uma nova tarefa.
        global task_id_counter
        data = request.json
        if not data.get("title"):
            return {"message": "Title is required"}, 400

        task = {
            "id": task_id_counter,
            "title": data["title"],
            "description": data.get("description", ""),
            "completed": False,
        }
        tasks[task_id_counter] = task
        task_id_counter += 1

        return task, 201

    def put(self, task_id):
        #Atualiza uma tarefa existente.
        task = tasks.get(task_id)
        if not task:
            return {"message": "Task not found"}, 404

        data = request.json
        task["title"] = data.get("title", task["title"])
        task["description"] = data.get("description", task["description"])
        task["completed"] = data.get("completed", task["completed"])

        return task, 200

    def delete(self, task_id):
        # Deleta uma tarefa existente.
        if task_id not in tasks:
            return {"message": "Task not found"}, 404
        del tasks[task_id]
        return {"message": "Task deleted"}, 200


# Configurando as rotas
api.add_resource(Task, "/tasks", "/tasks/<int:task_id>")

if __name__ == "__main__":
    app.run(debug=True)
