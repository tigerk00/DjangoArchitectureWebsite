from django.test import TestCase
import tempfile
from news.models import News, NewsFile, NewsShot
import datetime


class NewsTestCase(TestCase):
    def setUp(self):
        self.news = News.objects.create(title="Test_news_name1",
                                        description="Test description",
                                        poster=tempfile.NamedTemporaryFile(suffix=".jpg").name,
                                        url="test_work_name1",
                                        draft=False,
                                        source="source_test",
                                        important=True,
                                        date=datetime.datetime.now(),
                                        )

        self.news_file = NewsFile.objects.create(title="Test_news_name2",
                                                description="Test description",
                                                file=tempfile.NamedTemporaryFile(suffix=".jpg").name,
                                                news=self.news,
                                                )
        self.news_shot = NewsShot.objects.create(title="Test_news_name3",
                                                description="Test description",
                                                image=tempfile.NamedTemporaryFile(suffix=".jpg").name,
                                                news=self.news,
                                                )

    def test_news_was_correctly_built(self):
        """Testing News-Model Object"""
        news_test = News.objects.get(title="Test_news_name1")
        news_file_test = NewsFile.objects.get(pk=1)
        news_shot_test = NewsShot.objects.get(pk=1)
        self.assertEqual(news_file_test.news, news_test)
        self.assertEqual(news_shot_test.news, news_test)

