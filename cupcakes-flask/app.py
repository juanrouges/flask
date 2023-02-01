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
  all_cupcakes = [cupcake.serialize() for cupcake in Cupcake.query.all()]
  return jsonify(cupcakes=all_cupcakes)

@app.route("/api/cupcakes/<int:id>")
def details_cupcake(id):
  cupcake = Cupcake.query.get_or_404(id).serialize()
  return jsonify(cupcake=cupcake)

@app.route("/api/cupcakes", methods=["POST"])
def create_cupcake():
  new_cupcake = Cupcake(flavor = request.json["flavor"], 
                        size = request.json["size"], 
                        rating = request.json["rating"], 
                        image = request.json["image"])
  db.session.add(new_cupcake)
  db.session.commit()
  response_json = jsonify(new_cupcake.serialize())
  return (response_json, 201)