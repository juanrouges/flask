from flask import Flask, jsonify
from models import db, connect_db, Todo
# from forms import PetForm

app = Flask(__name__)
app.app_context().push()

app.config["SQLALCHEMY_DATABASE_URI"]         = "postgresql:///todosdb"
app.config["SECRET_KEY"]                      = "lamargarina321"
app.config["DEBUG"]                           = False
app.config["TEMPLATES_AUTO_RELOAD"]           = True
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]  = False
app.config["DEBUG_TB_INTERCEPT_REDIRECTS"]    = False
app.config["SQLALCHEMY_ECHO"]                 = False

connect_db(app)

@app.route("/api/todos")
def list_todos():
  all_todos = [todo.serialize() for todo in Todo.query.all()]
  return jsonify(todos=all_todos)

@app.route("/api/todos/<int:id>")
def get_todo(id):
  todo = Todo.query.get_or_404(id).serialize()
  return jsonify(todo=todo)