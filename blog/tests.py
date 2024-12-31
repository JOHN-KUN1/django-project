from django.test import TestCase, Client
from .models import Blogs
from django.contrib.auth.models import User

# Create your tests here.

class TestModels(TestCase):
    def test_blog_model(self):
        user = User.objects.create_user(username="testuser",password="password94000")

        blog_post = Blogs.objects.create(
            title = "This is a test blog post",
            content = "This is a blog post made from testing the app",
            author = user
        ) 
        self.assertEqual(str(blog_post),"This is a test blog post")
        self.assertTrue(isinstance(blog_post,Blogs))

