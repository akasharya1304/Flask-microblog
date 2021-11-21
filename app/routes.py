from flask import render_template
from app import app

@app.route("/")
@app.route("/index")
def index():
    user = {"username" : "Akash Kumar"}
    posts = [
        {
            "author" : {"username" : "John"},
            "body" : "Today is very cold day"
        },
        {
            "author" : {"username" : "Henry"},
            "body" : "Avenger movie is so cool"
        }
            ]
    return render_template("index.html", title="Home" , user=user , posts=posts)