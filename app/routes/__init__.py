from flask import render_template, request
from app import app
from app.models import User

@app.route("/", methods=['GET'])
def home():
    return render_template("home.html")
