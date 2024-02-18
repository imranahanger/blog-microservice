# /blog_microservice/app/models/blog_post.py
from flask_mongoengine import MongoEngine

db = MongoEngine()

class BlogPost(db.Document):
    title = db.StringField(required=True, max_length=100)
    content = db.StringField(required=True)
    author = db.StringField(required=True, max_length=50)
