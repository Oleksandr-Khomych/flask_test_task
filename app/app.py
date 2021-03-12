from config import Configuration

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import request, redirect, url_for

from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from flask_security import SQLAlchemyUserDatastore, Security, current_user


app = Flask(__name__)
app.config.from_object(Configuration)

db = SQLAlchemy(app)

migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)


# Adminka
from flask_admin import Admin
from flask_admin import AdminIndexView
from flask_admin.contrib.sqla import ModelView
from models import Author, Book, User, Role


class AdminMixin:
    def is_accessible(self):
        return current_user.has_role('admin')

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('security.login', next=request.url))


class AdminView(AdminMixin, ModelView):
    pass


class HomeAdminView(AdminMixin, AdminIndexView):
    pass


admin = Admin(app, 'AdminMenu', url='/admin/', index_view=HomeAdminView())

admin.add_view(AdminView(Author, db.session))
admin.add_view(AdminView(Book, db.session))


# flask_security
user_datastore = SQLAlchemyUserDatastore(db, User, Role)

security = Security(app, user_datastore)
