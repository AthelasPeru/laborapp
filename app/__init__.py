from flask import Flask, request, abort
from flask.ext.security import Security, SQLAlchemyUserDatastore
from flask_debugtoolbar import DebugToolbarExtension
from flask_admin import Admin


from app.models import db
from app.models.user import User
from app.models.role import Role
from app.models.skill import Skill

from app.blueprints.admin.views import AdminUserView, AdminSkillView, AdminRoleView


# extensions
debug = DebugToolbarExtension()
admin = Admin()


# blueprints
from app.blueprints.front.views import front
from app.blueprints.front.forms import ExtendedRegisterForm
from app.blueprints.dashboard.views import dashboard


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
    debug.init_app(app)
    db.init_app(app)
    admin = Admin(app, name='Laborapp', template_mode='bootstrap3')

    # Setup Flask-Security
    user_datastore = SQLAlchemyUserDatastore(db, User, Role)
    security = Security(
        app, user_datastore, register_form=ExtendedRegisterForm)

    # Blueprints
    app.register_blueprint(front)
    app.register_blueprint(dashboard)

    # Admin Blueprints
    admin.add_view(AdminSkillView(Skill, db.session))
    admin.add_view(AdminRoleView(Role, db.session))
    admin.add_view(AdminUserView(User, db.session))

    # Context Processors
    @security.register_context_processor
    def security_register_processor():
        role = request.args.get("role", None)
        if role:
            role_id = db.session.query(Role).filter_by(name=role).first().id
            if role_id:
                return dict(
                    role=role,
                    role_id=role_id
                )
                
        return dict(role=role)
        # else:
        #     abort(500)



    return app
