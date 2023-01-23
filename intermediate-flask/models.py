from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
  db.app = app
  db.init_app(app)

class Employee(db.Model):
  __tablename__ = "employees"

  id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  name = db.Column(db.Text, nullable=False)
  province = db.Column(db.String(50), nullable=False, default="ON")
  department = db.Column(db.String(50), nullable=False, default="operations")
  salary = db.Column(db.Float, nullable=False, default=40000.25)

class Department(db.Model):
  __tablename__ = "departments"

  dept_code = db.Column(db.String, primary_key=True, unique=True)
  dept_name = db.Column(db.Text, nullable=False)
  dept_phone = db.Column(db.String(20))