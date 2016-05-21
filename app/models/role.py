from app.models import db


class Role(db.Model):

    """	
    Basic Role model
    """

    __tablename__ = "roles"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Unicode(50), unique=True)
    description = db.Column(db.UnicodeText)

    def __repr__(self):
        return "{}: {}".format(self.name, self.description)
