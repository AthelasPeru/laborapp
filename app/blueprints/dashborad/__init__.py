from flask import Blueprint, render_template


dashboard = Blueprint("dashboard", __name__, url_prefix="user")

@dashboard
def main():
	return render_template("dashboard/index.html")