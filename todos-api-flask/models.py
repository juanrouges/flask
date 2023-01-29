from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
  db.app = app
  db.init_app(app)

class Todo(db.Model):
  __tablename__ = "todos"

  def __rep__(self):
    return f"<Todo id={self.id} title={self.title} done={self.done} >"

  id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  title = db.Column(db.Text, nullable=False)
  done = db.Column(db.Boolean, default=False, nullable=False)

  def serialize(self):
    return { "name": self.id, 
              "title": self.title, 
              "done": self.done
            }