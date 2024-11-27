from flask_cors import CORS
from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity

app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = "sua_chave_secreta"  # Altere para uma chave segura
jwt = JWTManager(app)
api = Api(app)

# Simulação de banco de dados
users = {"admin": "senha123"}
tasks = {}
task_id_counter = 1

# Rota de autenticação
class Login(Resource):
    def post(self):
        data = request.json
        username = data.get("username")
        password = data.get("password")

        if username in users and users[username] == password:
            token = create_access_token(identity=username)
            return {"access_token": token}, 200
        return {"message": "Invalid username or password"}, 401

# Rota de tarefas protegida por autenticação
class Task(Resource):
    @jwt_required()
    def get(self, task_id=None):
        if task_id:
            task = tasks.get(task_id)
            if not task:
                return {"message": "Task not found"}, 404
            return task, 200
        return tasks, 200

    @jwt_required()
    def post(self):
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

    @jwt_required()
    def put(self, task_id):
        task = tasks.get(task_id)
        if not task:
            return {"message": "Task not found"}, 404

        data = request.json
        task["title"] = data.get("title", task["title"])
        task["description"] = data.get("description", task["description"])
        task["completed"] = data.get("completed", task["completed"])

        return task, 200

    @jwt_required()
    def delete(self, task_id):
        if task_id not in tasks:
            return {"message": "Task not found"}, 404
        del tasks[task_id]
        return {"message": "Task deleted"}, 200


# Configurando as rotas
api.add_resource(Login, "/login")
api.add_resource(Task, "/tasks", "/tasks/<int:task_id>")

if __name__ == "__main__":
    app.run(debug=True)
