# /blog_microservice/app/services/blog_service.py
from app.models.blog_post import BlogPost

class BlogService:
    @staticmethod
    def create_blog_post(title, content, author):
        blog_post = BlogPost(title=title, content=content, author=author)
        blog_post.save()
        return blog_post

    @staticmethod
    def get_blog_posts():
        return BlogPost.objects()
