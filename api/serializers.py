from rest_framework import serializers
from arch_works.models import Architecture, ArchitectureShots, Architector, Style
from blog.models import Blog, BlogShot, BlogFile
from my_works.models import Work, WorkShot, WorkFile
from news.models import News, NewsShot, NewsFile



#API Serializer Архитектуры
class ArchSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('title', 'description', 'main_photo', 'year', 'country', 'architectors', 'styles', 'budget', 'url', 'draft',)
        lookup_field = 'url'
        model = Architecture



#API Serializer Кадров Архитектуры
class ArchShotSerializer(serializers.ModelSerializer):

    architecture_name = serializers.CharField(source='architecture.title', read_only=True)

    class Meta:
        fields = ('title', 'description', 'image', 'architecture', 'architecture_name',)
        model = ArchitectureShots



#API Serializer Архитектора
class ArchitectSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('name', 'country', 'date_of_birth', 'date_of_death', 'description', 'image', 'url', 'draft')
        lookup_field = 'url'
        model = Architector



#API Serializer Стилей Архитектуры
class StyleSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('name', 'description', 'image', 'url', 'draft',)
        lookup_field = 'url'
        model = Style



#API Serializer Блога
class BlogSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('title', 'poster', 'description', 'date', 'draft', 'url')
        lookup_field = 'url'
        model = Blog



#API Serializer Кадров Блога
class BlogShotSerializer(serializers.ModelSerializer):

    blog_name = serializers.CharField(source='blog.title', read_only=True)

    class Meta:
        fields = ('title', 'description', 'image', 'blog', 'blog_name',)
        model = BlogShot



#API Serializer Файлов Блога
class BlogFileSerializer(serializers.ModelSerializer):

    blog_name = serializers.CharField(source='blog.title', read_only=True)

    class Meta:
        fields = ('title', 'description', 'file', 'blog', 'blog_name',)
        model = BlogFile



#API Serializer Работы
class WorkSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('title', 'main_photo', 'description', 'draft', 'url')
        lookup_field = 'url'
        model = Work



#API Serializer Кадров Работы
class WorkShotSerializer(serializers.ModelSerializer):

    work_name = serializers.CharField(source='work.title', read_only=True)

    class Meta:
        fields = ('title', 'description', 'image', 'work', 'work_name',)
        model = WorkShot



#API Serializer Файлов Работ
class WorkFileSerializer(serializers.ModelSerializer):

    work_name = serializers.CharField(source='work.title', read_only=True)

    class Meta:
        fields = ('title', 'description', 'file', 'work', 'work_name',)
        model = WorkFile



#API Serializer Новости
class NewsSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('title', 'poster', 'description', 'date', 'draft', 'url', 'source', 'important')
        model = News


#API Serializer Кадров Новости
class NewsShotSerializer(serializers.ModelSerializer):

    news_name = serializers.CharField(source='news.title', read_only=True)

    class Meta:
        fields = ('title', 'description', 'image', 'news', 'news_name',)
        model = NewsShot



#API Serializer Файлов Новости
class NewsFileSerializer(serializers.ModelSerializer):

    news_name = serializers.CharField(source='news.title', read_only=True)

    class Meta:
        fields = ('title', 'description', 'file', 'news', 'news_name',)
        model = NewsFile