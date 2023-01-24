from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SelectField
from wtforms.validators import InputRequired, Optional

class AddEmployeeForm(FlaskForm):
  """for to create a new employee"""
  name = StringField("Name", validators=[InputRequired()])
  province = SelectField("Province", validators=[InputRequired()])
  department = SelectField("Department", validators=[InputRequired()])
  salary = FloatField("Salary", validators=[InputRequired()])