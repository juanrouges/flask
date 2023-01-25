from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SelectField, BooleanField
from wtforms.validators import InputRequired, Optional, DataRequired
from wtforms.widgets import TextArea

class PetForm(FlaskForm):
  """form to add new pet"""
  name = StringField("Name", validators=[InputRequired()])
  species = StringField("Species", validators=[InputRequired()])
  photo_url = StringField("Image", validators=[Optional()])
  age = StringField("Age", validators=[Optional()])
  notes = StringField("Notes", widget=TextArea(), validators=[Optional()])
  available = BooleanField("Is it available for adoption?", default=True)