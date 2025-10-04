from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    
    # --- Config ---
    app.config['SECRET_KEY'] = 'supersecretkey'   # for forms/session
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///inventory.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # --- Initialize DB ---
    db.init_app(app)

    # --- Import and register routes ---
    from .routes import main
    app.register_blueprint(main)

    # --- Create DB tables ---
    with app.app_context():
        db.create_all()

    return app
