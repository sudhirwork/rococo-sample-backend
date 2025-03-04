from flask import Flask
from app.database import init_db
from app.routes import api_routes

def create_app():
    app = Flask(__name__)

    # Initialize database
    init_db()

    # Register API routes
    app.register_blueprint(api_routes)

    return app
