from flask import Flask, jsonify, request
from models import db, connect_db, Cupcake
# from forms import PetForm

app = Flask(__name__)
app.app_context().push()

app.config["SQLALCHEMY_DATABASE_URI"]         = "postgresql:///cupcakesdb"
app.config["SECRET_KEY"]                      = "worldcalssbakers"
app.config["DEBUG"]                           = True
app.config["TEMPLATES_AUTO_RELOAD"]           = True
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]  = False
app.config["DEBUG_TB_INTERCEPT_REDIRECTS"]    = False
app.config["SQLALCHEMY_ECHO"]                 = False

connect_db(app)

@app.route("/api/cupcakes")
def list_cupcakes():
  return ("Hello World!")