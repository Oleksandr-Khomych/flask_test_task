from config import Configuration

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from flask_security import SQLAlchemyUserDatastore, Security


app = Flask(__name__)
app.config.from_object(Configuration)

db = SQLAlchemy(app)

migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)


# Adminka
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from models import Author, Book, User, Role

admin = Admin(app)

admin.add_view(ModelView(Author, db.session))
admin.add_view(ModelView(Book, db.session))


# flask_security

user_datastore = SQLAlchemyUserDatastore(db, User, Role)

security = Security(app, user_datastore)
