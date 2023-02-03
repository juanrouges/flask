from flask import Flask, render_template

app =Flask(__name__)

app.config["DEBUG"]                           = True
app.config["TEMPLATES_AUTO_RELOAD"]           = True
app.config["SECRET_KEY"]                      = "opalinula456!"

@app.route("/")
def feedback_stream():
    return render_template("index.html")