from flask.ext.security import RoleMixin
from app.models import db


class Role(db.Model, RoleMixin):

    """	
    Basic Role model
    """

    __tablename__ = "roles"

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.Unicode(80), unique=True)
    description = db.Column(db.UnicodeText)

    def __repr__(self):
        return "{}: {}".format(self.name, self.description)


