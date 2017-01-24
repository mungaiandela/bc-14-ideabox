from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import app_config
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap
<<<<<<< HEAD
from flask_pagedown import PageDown
=======
>>>>>>> b55bd1732826a6919470cb2ebc5c73e9d9081570

db = SQLAlchemy()
login_manager = LoginManager()


def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    Bootstrap(app)
    db.init_app(app)
<<<<<<< HEAD

=======
    # login code
>>>>>>> b55bd1732826a6919470cb2ebc5c73e9d9081570
    login_manager.init_app(app)
    login_manager.login_message = "You must be logged in to have access"
    login_manager.login_view = "auth.login"

    migrate = Migrate(app, db)

<<<<<<< HEAD
    pagedown = PageDown(app)

=======
>>>>>>> b55bd1732826a6919470cb2ebc5c73e9d9081570
    from app import models

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    from .home import home as home_blueprint
    app.register_blueprint(home_blueprint)

    return app
