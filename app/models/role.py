from app.models import db


class Role(db.Model):

	__tablename__ = "roles"

	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.Unicode(20), unique=True)