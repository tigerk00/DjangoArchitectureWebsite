from django.urls import path
from .views import Home, Detail

app_name = "news"
urlpatterns = [
    path("", Home.as_view(), name="news_home"),
    path("<str:url>", Detail.as_view(), name="news_detail"),
]