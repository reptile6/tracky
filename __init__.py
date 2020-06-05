from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

# Instantiate SQL_Alchemy DB
db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')

    db.init_app(app)

    # Instantiate Login Manager to help with authentication
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    # Import user model for user querying
    from models import User

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    # Import and register blueprints for routing
    from views import auth, main
    app.register_blueprint(auth)
    app.register_blueprint(main)

    return app
