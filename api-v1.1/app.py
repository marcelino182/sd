from flask_cors import CORS
from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://username:password@localhost/todo_app"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["JWT_SECRET_KEY"] = "sua_chave_secreta"

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)
api = Api(app)
#CORS(app)
# liberar comunicação de qualquer origem com CORS em flask
cors = CORS(app, resources={r"/*": {"origins": "*"}})

# Modelos
class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)


class Task(db.Model):
    __tablename__ = "tasks"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text)
    completed = db.Column(db.Boolean, default=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)

# Inicializar banco de dados
with app.app_context():
    db.create_all()

class Login(Resource):
    def post(self):
        data = request.json
        username = data.get("username")
        password = data.get("password")

        user = User.query.filter_by(username=username).first()
        if user and bcrypt.check_password_hash(user.password, password):
            token = create_access_token(identity=user.id)
            return {"access_token": token}, 200
        return {"message": "Invalid username or password"}, 401
class Register(Resource):
    def post(self):
        data = request.json
        username = data.get("username")
        password = data.get("password")

        if User.query.filter_by(username=username).first():
            return {"message": "Username already exists"}, 400

        hashed_password = bcrypt.generate_password_hash(password).decode("utf-8")
        new_user = User(username=username, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        return {"message": "User created successfully"}, 201
class Task(Resource):
    @jwt_required()
    def get(self, task_id=None):
        user_id = get_jwt_identity()
        if task_id:
            task = Task.query.filter_by(id=task_id, user_id=user_id).first()
            if not task:
                return {"message": "Task not found"}, 404
            return {
                "id": task.id,
                "title": task.title,
                "description": task.description,
                "completed": task.completed,
            }, 200

        tasks = Task.query.filter_by(user_id=user_id).all()
        return [
            {
                "id": task.id,
                "title": task.title,
                "description": task.description,
                "completed": task.completed,
            }
            for task in tasks
        ], 200

    @jwt_required()
    def post(self):
        data = request.json
        if not data.get("title"):
            return {"message": "Title is required"}, 400

        user_id = get_jwt_identity()
        new_task = Task(
            title=data["title"],
            description=data.get("description", ""),
            completed=False,
            user_id=user_id,
        )
        db.session.add(new_task)
        db.session.commit()

        return {
            "id": new_task.id,
            "title": new_task.title,
            "description": new_task.description,
            "completed": new_task.completed,
        }, 201

    @jwt_required()
    def put(self, task_id):
        user_id = get_jwt_identity()
        task = Task.query.filter_by(id=task_id, user_id=user_id).first()
        if not task:
            return {"message": "Task not found"}, 404

        data = request.json
        task.title = data.get("title", task.title)
        task.description = data.get("description", task.description)
        task.completed = data.get("completed", task.completed)

        db.session.commit()
        return {
            "id": task.id,
            "title": task.title,
            "description": task.description,
            "completed": task.completed,
        }, 200

    @jwt_required()
    def delete(self, task_id):
        user_id = get_jwt_identity()
        task = Task.query.filter_by(id=task_id, user_id=user_id).first()
        if not task:
            return {"message": "Task not found"}, 404

        db.session.delete(task)
        db.session.commit()
        return {"message": "Task deleted"}, 200
    
api.add_resource(Register, "/register")
api.add_resource(Login, "/login")
api.add_resource(Task, "/tasks", "/tasks/<int:task_id>")

from flask import send_from_directory

@app.route('/')
def serve_frontend():
    return send_from_directory('frontend', 'index.html')

@app.route('/<path:path>')
def serve_static_files(path):
    return send_from_directory('frontend', path)

if __name__ == "__main__":
    app.run(debug=True)
