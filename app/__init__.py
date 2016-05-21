from flask import Flask 
from flask.ext.security import Security, SQLAlchemyUserDatastore, \
    UserMixin, RoleMixin, login_required



def create_app(app=None, config_file=None):
	"""
	factory that instantiates the app
	"""

	if not app:
		app = Flask(__name__)

	# config files
	app.config.from_pyfile("config/base.py")
	if config_file:
		app.config.from_pyfile("config/{}.py".format(config_file))

	# extensions

	# Blueprints
	
