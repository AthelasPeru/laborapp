import os

# DATABASE SETTINGS
SQLALCHEMY_DATABASE_URI = 'sqlite:////{}/laborapp.db'.format(os.getcwd())

SECRET_KEY = "withgreatpowercomesgreatresponsibility"

DEBUG = True