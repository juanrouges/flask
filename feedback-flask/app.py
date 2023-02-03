from flask import Flask, render_template
from models import db, connect_db, User

app =Flask(__name__)
app.app_context().push()

app.config["SQLALCHEMY_DATABASE_URI"]         = "postgresql:///feedbackdb"
app.config["DEBUG"]                           = True
app.config["TEMPLATES_AUTO_RELOAD"]           = True
app.config["SECRET_KEY"]                      = "opalinula456!"

connect_db(app)

@app.route("/")
def feedback_stream():
    return render_template("index.html")