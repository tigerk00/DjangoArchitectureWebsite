from rest_framework import viewsets, generics
from .serializers import *


# Architecture
class ArchViewSet(viewsets.ModelViewSet):
    queryset = Architecture.objects.all()
    serializer_class = ArchSerializer
    lookup_field = 'url'


# Architecture-Shot
class ArchShotViewSet(viewsets.ModelViewSet):
    queryset = ArchitectureShots.objects.all()
    serializer_class = ArchShotSerializer


# Architect
class ArchitectViewSet(viewsets.ModelViewSet):
    queryset = Architector.objects.all()
    serializer_class = ArchitectSerializer
    lookup_field = 'url'


# Style
class StyleViewSet(viewsets.ModelViewSet):
    queryset = Style.objects.all()
    serializer_class = StyleSerializer
    lookup_field = 'url'


# Blog
class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    lookup_field = 'url'


# Blog-Shot
class BlogShotViewSet(viewsets.ModelViewSet):
    queryset = BlogShot.objects.all()
    serializer_class = BlogShotSerializer


# Blog-File
class BlogFileViewSet(viewsets.ModelViewSet):
    queryset = BlogFile.objects.all()
    serializer_class = BlogFileSerializer



# Work
class WorkViewSet(viewsets.ModelViewSet):
    queryset = Work.objects.all()
    serializer_class = WorkSerializer
    lookup_field = 'url'


# Work-Shot
class WorkShotViewSet(viewsets.ModelViewSet):
    queryset = WorkShot.objects.all()
    serializer_class = WorkShotSerializer


# Work-File
class WorkFileViewSet(viewsets.ModelViewSet):
    queryset = WorkFile.objects.all()
    serializer_class = WorkFileSerializer


# News
class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer


# News-Shot
class NewsShotViewSet(viewsets.ModelViewSet):
    queryset = NewsShot.objects.all()
    serializer_class = NewsShotSerializer


# News-File
class NewsFileViewSet(viewsets.ModelViewSet):
    queryset = NewsFile.objects.all()
    serializer_class = NewsFileSerializer

