# /blog_microservice/app/__init__.py
from flask import Flask
from flask_mongoengine import MongoEngine
from app.config.config import Config
from app.routes.blog_routes import register_routes

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db = MongoEngine(app)
    register_routes(app)

    return app
