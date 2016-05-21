from app.models import db


class User(db.Model):

    """	
    Basic skill model
    """

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Unicode(50), unique=True)
    email = db.Column(db.Unicode(120), unique=True)
    password = db.Column(db.Unicode(120))

    roles = db.relationship('Role', secondary=roles_users,
        backref=db.backref('users', lazy='dynamic'))

    def __repr__(self):
        return "{}: {}".format(self.name, self.email)
