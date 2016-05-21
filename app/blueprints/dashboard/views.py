from flask import Blueprint, render_template
from flask_security import login_required
from flask_security.core import current_user

from app.blueprints.dashboard.forms import SkillsForm

dashboard = Blueprint("dashboard", __name__, url_prefix="/user")


@dashboard.route("/dashboard", methods=["GET", "POST"])
@login_required
def main():

    form = SkillsForm()


    return render_template(
        
        "dashboard/index.html",
        user=current_user,
    )
