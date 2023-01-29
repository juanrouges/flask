from flask import Flask, render_template, redirect, flash
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

@app.route("/")
def index():
  return render_template("index.html")