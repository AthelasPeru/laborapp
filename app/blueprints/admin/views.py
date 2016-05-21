from flask_admin.contrib.sqla import ModelView


class AdminUserView(ModelView):

    """Vista que permite realizar operaciones CRUD sobre el modelo User"""

    column_list = ("name", "email", "skills", "roles")


class AdminRoleView(ModelView):

    """Vista que permite realizar operaciones CRUD sobre el modelo Role"""

    column_list = ("name", "description")


class AdminSkillView(ModelView):

    column_list = ("name", "description")
