# /blog_microservice/app/use_cases/create_blog_post.py
from app.services.blog_service import BlogService

class CreateBlogPostUseCase:
    @staticmethod
    def execute(title, content, author):
        return BlogService.create_blog_post(title, content, author)
