from django.urls import path
from .views import Home, Detail

app_name = "my_works"
urlpatterns = [
    path("", Home.as_view(), name="my_works_home"),
    path("<slug:url>", Detail.as_view(), name="my_works_detail"),
]