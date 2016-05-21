from flask import Blueprint, render_template

from flask_security import login_required

front = Blueprint("front", __name__)

@front.route("/")
def index():
	return render_template("front/index.html")

@front.route("/secure")
@login_required
def admin():
	return render_template("front/index.html")

