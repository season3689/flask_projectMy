import os
from pathlib import Path
from flask import Flask
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect



db= SQLAlchemy()
csrf = CSRFProtect()

login_manager = LoginManager() 
login_manager.login_view = "auth.signup"
login_manager.login_message = ""

app = Flask(__name__)
def create_app():


    app.config.from_mapping(
        SECRET_KEY="znlwmdi",
        SQLALCHEMY_DATABASE_URI=
        f"sqlite:///{Path(__file__).parent.parent / 'local.sqlite'}",
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
        SQLALCHEMY_ECHO=True,
        WTF_CSRF_SECRET_KEY="3asdfg3asdfg3asdfg",
    )
    

    db.init_app(app)
    
    Migrate(app, db)
    csrf.init_app(app)
    login_manager.init_app(app)

    from apps.quiz import views as quiz_views

    app.register_blueprint(quiz_views.quiz, url_prefix="/quiz")

    return app

