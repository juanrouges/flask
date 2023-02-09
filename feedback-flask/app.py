from flask import Flask, render_template, redirect, flash, session
from models import db, connect_db, User
from forms import RegisterForm, LoginForm

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

# FEEDBACK
@app.route("/feedback")
def feedback_rules():
    if "user_id" not in session:
        flash("Please login first!")

        return redirect("/login")

    return render_template("/feedback.html")

# LOGIN
@app.route("/login", methods=["GET", "POST"])
def user_login():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        user = User.authenticate(username, password)
        if user:
            flash(f"Welcome {user.first_name}")
            session["user_id"] = user.id

            return redirect("/feedback")
        else:
            form.username.errors = ["Invalid Username/Password"]
    
    return render_template("login.html", form=form)

# Logout
@app.route("/logout")
def user_logout():
    session.pop("user_id")
    flash("Succesfully logged out!")
    return redirect("/login")
    

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

        flash("Your account was succesful created! Login now.")

        return redirect("/login")
    else:
        return render_template("register.html", form=form)