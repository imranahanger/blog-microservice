# /blog_microservice/app/controllers/blog_controller.py
from flask import Blueprint, jsonify, request
from app.use_cases.create_blog_post import CreateBlogPostUseCase
from app.use_cases.get_blog_posts import GetBlogPostsUseCase

blog_bp = Blueprint('blog', __name__, url_prefix='/blog')

@blog_bp.route('/create', methods=['POST'])
def create_blog_post():
    data = request.get_json()
    title = data.get('title')
    content = data.get('content')
    author = data.get('author')

    blog_post = CreateBlogPostUseCase.execute(title, content, author)

    return jsonify({'message': 'Blog post created successfully', 'blog_post': blog_post.to_json()}), 201

@blog_bp.route('/get', methods=['GET'])
def get_blog_posts():
    blog_posts = GetBlogPostsUseCase.execute()
    blog_posts_json = [blog_post.to_json() for blog_post in blog_posts]

    return jsonify({'blog_posts': blog_posts_json})
