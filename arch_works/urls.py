from django.urls import path
from . import views

urlpatterns = [
    path("", views.Home.as_view(), name="home"),
    path("search", views.Search.as_view(), name="search"),
    path("architectors", views.architectors, name="architectors"),
    path("architectors/<str:url>", views.architector_detail, name="architector_detail"),
    path("styles", views.styles, name="styles"),
    path("styles/<str:url>", views.style_detail, name="style_detail"),
    path("<str:url>", views.arch_detail, name="arch_detail"),
]