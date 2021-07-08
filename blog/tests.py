from django.test import TestCase
import tempfile
from blog.models import Blog, BlogShot, BlogFile


class BlogTestCase(TestCase):
    def setUp(self):
        self.blog = Blog.objects.create(title="Test_blog_name1",
                                        description="Test description",
                                        poster=tempfile.NamedTemporaryFile(suffix=".jpg").name,
                                        url="test_blog_name1",
                                        draft=False)

        self.blog_file = BlogFile.objects.create(title="Test_blog_name2",
                                                 description="Test description",
                                                 file=tempfile.NamedTemporaryFile(suffix=".jpg").name,
                                                 blog=self.blog,
                                                 )

        self.blog_shot = BlogShot.objects.create(title="Test_blog_name3",
                                                 description="Test description",
                                                 image=tempfile.NamedTemporaryFile(suffix=".jpg").name,
                                                 blog=self.blog,
                                                 )

    def test_blog_was_correctly_built(self):
        """Testing Blog-Model Object"""
        blog_test = Blog.objects.get(url="test_blog_name1")
        blog_file_test = BlogFile.objects.get(pk=1)
        blog_shot_test = BlogShot.objects.get(pk=1)
        self.assertEqual(blog_test.title, "Test_blog_name1")
        self.assertEqual(blog_file_test.blog, blog_test)
        self.assertEqual(blog_shot_test.blog, blog_test)
