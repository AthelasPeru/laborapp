from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_security import login_required
from flask_security.core import current_user

from app.blueprints.dashboard.forms import SkillsForm

from app.models import db
from app.models.skill import Skill
from app.models.user import User


from app.blueprints.dashboard.utils import matching_companies

dashboard = Blueprint("dashboard", __name__, url_prefix="/user")


@dashboard.route("/dashboard", methods=["GET", "POST"])
@login_required
def main():

    user = db.session.query(User).get(current_user.id)
    skills = db.session.query(Skill).all()
    skills_form = SkillsForm()
    skills_form.skills.choices = [
        (skill.id, skill.name.capitalize()) for skill in skills]

    if request.method == "GET":
        companies = matching_companies(user)
        

        return render_template(

            "dashboard/index.html",
            user=user,
            skills_form=skills_form,
            companies=companies
        )

    elif request.method == "POST":
        if skills_form.validate_on_submit():

            

                user.skills = []
                db.session.commit()
                for skill in skills_form.skills.data:
                    skill = db.session.query(Skill).get(skill)
                    user.skills.append(skill)

                db.session.commit()
                flash("Data agregada correctamente")
                return redirect(url_for("dashboard.main"))
        elif skills_form.errors:
            print "errores {}".format(skills_form.errors)
            flash("Data erronea {}".format(skills_form.errors))
            return redirect(url_for("dashboard.main"))
