from flask_wtf import Form 
from app.utils.forms import MultiCheckboxField
from wtforms import TextField
from wtforms.validators import Required

class SkillsForm(Form):

	skills = MultiCheckboxField(
		"Categorias",
		coerce=int
	)
