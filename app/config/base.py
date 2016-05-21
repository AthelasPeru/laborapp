import os

# DATABASE SETTINGS
SQLALCHEMY_DATABASE_URI = 'sqlite:////{}/laborapp.db'.format(os.getcwd())

SECRET_KEY = "withgreatpowercomesgreatresponsibility"

DEBUG = True

# mail settings
MAIL_SERVER = 'smtp.example.com'
MAIL_PORT = 465
MAIL_USE_SSL = True
MAIL_USERNAME = 'username'
MAIL_PASSWORD = 'password'

# Flask Security Settings
SECURITY_REGISTERABLE = True
