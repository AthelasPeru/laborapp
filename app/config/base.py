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
SECURITY_SEND_REGISTER_EMAIL = False
SECURITY_SEND_PASSWORD_CHANGE_EMAIL = False
SECURITY_SEND_PASSWORD_RESET_NOTICE_EMAIL = False
SECURITY_LOGIN_WITHOUT_CONFIRMATION = True

SECURITY_POST_LOGIN_VIEW = "/user/dashboard"

SKILLS = ['PHP', 'Java', 'Ruby', 'C#', 'C++', 'Bash', 'SQL', 'CSS', 'HTML', 'QA', 'Node', 'Flask', 'PHP', 'JavaScript', 'Java', 'Ruby', 'C#', 'C++', 'Bash', 'SQL', 'CSS', 'HTML', 'QA', 'Node', 'Flask',]
