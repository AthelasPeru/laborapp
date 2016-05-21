from flask import Flask, request, abort
from flask.ext.security import Security, SQLAlchemyUserDatastore
from flask_security.core import current_user
from flask_security.signals import user_registered
from flask_debugtoolbar import DebugToolbarExtension
from flask_admin import Admin


from app.models import db
from app.models.user import User
from app.models.role import Role
from app.models.skill import Skill

from app.blueprints.admin.views import AdminUserView, AdminSkillView, AdminRoleView

# blueprints
from app.blueprints.front.views import front
from app.blueprints.front.forms import ExtendedRegisterForm
from app.blueprints.dashboard.views import dashboard

# extensions
debug = DebugToolbarExtension()
admin = Admin()




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
    security = Security(app=app,
        datastore=user_datastore, register_form=ExtendedRegisterForm)
    

    

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

            

            # signal processors
            @user_registered.connect_via(app)
            def user_registered_sighandler(sender, role=role, **extra):
                
                user = extra.get('user')
                
                user_datastore.add_role_to_user(user,role)
                db.session.commit()
                

            
        return dict(role=role)
        # else:
        #     abort(500)

    @app.before_request
    def add_user_role():
        if hasattr(current_user, "id"):
            user = db.session.query(User).get(current_user.id)
            if not current_user.has_role("candidate") or \
                not current_user.has_role("company"):
                role = request.args.get("role", None)
                if role:
                    role_to_set = db.session.query(Role).filter_by(name=role).first()
                    user.roles.append(role_to_set)
                    db.session.commit()



    



    return app
