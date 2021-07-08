from django.urls import path
from .views import Home, Detail, AddReview

app_name = "blog"
urlpatterns = [
    path("", Home.as_view(), name="blog_home"),
    path("<str:url>", Detail.as_view(), name="blog_detail"),
    path("review/<str:url>", AddReview.as_view(), name="add_review"),
]