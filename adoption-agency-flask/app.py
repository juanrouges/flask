from flask import Flask, render_template, redirect, flash
from models import db, connect_db, Pet
# from forms import EmployeeForm
# from resources import UnitedStates

app = Flask(__name__)
app.app_context().push()

app.config["SQLALCHEMY_DATABASE_URI"]         = "postgresql:///adoptiondb"
app.config["SECRET_KEY"]                      = "fairanimaltreatment4568"
app.config["DEBUG"]                           = False
app.config["TEMPLATES_AUTO_RELOAD"]           = True
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]  = False
app.config["DEBUG_TB_INTERCEPT_REDIRECTS"]    = False
app.config["SQLALCHEMY_ECHO"]                 = False

connect_db(app)

@app.route("/")
def index():
  pets = Pet.query.all()
  return render_template("index.html", pets=pets)