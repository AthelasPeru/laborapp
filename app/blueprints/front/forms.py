# coding: utf-8

import sys  

reload(sys)  
sys.setdefaultencoding('utf8')


from flask_security.forms import RegisterForm
from wtforms import TextField
from wtforms.validators import Required

class ExtendedRegisterForm(RegisterForm):
	
	name = TextField("¿Cuál es tu nombre?", validators=[Required()])
	age = TextField("¿Cuál es tu edad?", validators=[Required()])
	proffession = TextField("¿Qué profesión tienes?", validators=[Required()])
