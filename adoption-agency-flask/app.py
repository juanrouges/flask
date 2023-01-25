from flask import Flask, render_template, redirect, flash
from models import db, connect_db, Pet
from forms import PetForm

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

@app.route("/add", methods=["GET", "POST"])
def pet_add():
  form = PetForm()
  if form.validate_on_submit():
    name      = form.name.data
    species   = form.species.data
    photo_url = form.photo_url.data
    age       = form.age.data
    notes     = form.notes.data
    available = form.available.data
    new_pet = Pet( name=name, 
                   species=species, 
                   photo_url=photo_url, 
                   age=age, 
                   notes=notes, 
                   available=available
                  )
    db.session.add(new_pet)
    db.session.commit()
    flash(f"{name} was added to adoption agency directory")
    return redirect("/")
  else:
    return render_template("pet_add.html", form=form)