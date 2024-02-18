# /blog_microservice/app/use_cases/get_blog_posts.py
from app.services.blog_service import BlogService

class GetBlogPostsUseCase:
    @staticmethod
    def execute():
        return BlogService.get_blog_posts()
