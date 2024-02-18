# /blog_microservice/app/routes/blog_routes.py
from app.controllers.blog_controller import blog_bp

def register_routes(app):
    app.register_blueprint(blog_bp)
