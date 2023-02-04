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

# FEEDBACK STREAM
@app.route("/")
def feedback_stream():
    return redirect("/register")

# REGISTRATION
@app.route("/register", methods=["GET", "POST"])
def user_register():
    form = RegisterForm()
    if form.validate_on_submit():
        username   = form.username.data
        password   = form.password.data
        email      = form.email.data
        first_name = form.first_name.data
        last_name  = form.last_name.data

        new_user = User.register(username, password, email, first_name, last_name)
        
        db.session.add(new_user)
        db.session.commit()

        return redirect("/about")
    else:
        return render_template("register.html", form=form)
    
# ABOUT
@app.route("/about")
def feedback_rules():
    return render_template("/about.html")