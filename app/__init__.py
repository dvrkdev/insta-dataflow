import os

from dotenv import load_dotenv
from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect

load_dotenv()

db = SQLAlchemy()
login_manager = LoginManager()
csrf = CSRFProtect()


def create_app():
    app = Flask(
        __name__,
        template_folder="templates",
        static_folder="static",
        static_url_path="/",
    )
    app.secret_key = os.environ.get("SECRET_KEY")
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///instagram_data.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)
    login_manager.init_app(app)
    csrf.init_app(app)

    from app.models import User

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(user_id)

    login_manager.login_view = "auth.login"
    login_manager.login_message = "Please log in to view this page!"
    login_manager.login_message_category = "info"

    # register blueprint routes to the app
    from app.routes import auth, dashboard

    app.register_blueprint(auth.bp)
    app.register_blueprint(dashboard.bp)

    return app
