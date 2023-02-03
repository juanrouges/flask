from flask import Flask, render_template, redirect
from models import db, connect_db, User
from forms import RegisterForm

app =Flask(__name__)
app.app_context().push()

app.config["SQLALCHEMY_DATABASE_URI"]         = "postgresql:///feedbackdb"
app.config["DEBUG"]                           = True
app.config["TEMPLATES_AUTO_RELOAD"]           = True
app.config["SECRET_KEY"]                      = "opalinula456!"

connect_db(app)

@app.route("/")
def feedback_stream():
    return redirect("/register")

@app.route("/register", methods=["GET", "POST"])
def user_register():
    form = RegisterForm()
    if form.validate_on_submit():
        print("form validated")
        return redirect("/about")
    else:
        return render_template("register.html", form=form)
    
@app.route("/about")
def feedback_rules():
    return redirect("/about")