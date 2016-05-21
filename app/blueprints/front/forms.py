from flask_security.forms import RegisterForm
from wtforms import TextField, SelectField
from wtforms.validators import Required, Optional, NumberRange, Length

class ExtendedRegisterForm(RegisterForm):
	