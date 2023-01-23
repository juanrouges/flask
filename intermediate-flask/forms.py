from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SelectField

class AddEmployeeForm(FlaskForm):
  """for to create a new employee"""
  name = StringField("Name")
  province = StringField("Province")
  department = SelectField("Department")
  salary = FloatField("Salary")