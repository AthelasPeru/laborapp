from app.models import db


roles_users = db.Table('roles_users',
        db.Column('user_id', db.Integer(), db.ForeignKey('users.id')),
        db.Column('role_id', db.Integer(), db.ForeignKey('roles.id')))

user_skills = db.Table("user_skills",
       db.Column(
           "user_id", db.Integer, db.ForeignKey("users.id")),
       db.Column(
           "skills_id", db.Integer, db.ForeignKey("skills.id"))
       )
