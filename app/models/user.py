from flask.ext.security import UserMixin

from app.models import db
from app.models.relationships import roles_users, user_skills


class User(db.Model, UserMixin):

    """	
    Basic user model

    """

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    active = db.Column(db.Boolean())
    confirmed_at = db.Column(db.DateTime())
    roles = db.relationship('Role', secondary=roles_users,
        backref=db.backref('users', lazy='dynamic'))
    skills = db.relationship("Skill",
        secondary=user_skills,
        backref=db.backref("users", lazy='dynamic'))

    def __repr__(self):
        return "{}: {}".format(self.name, self.email)
