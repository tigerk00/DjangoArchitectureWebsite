"""architect URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

admin.autodiscover()
admin.site.enable_nav_sidebar = False



schema_view = get_schema_view(
    openapi.Info(
        title="My Architecture Site API",
        default_version="v1",
        description="A sample API for working with Architecture Site",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="kostia.lagoda@gmail.com"),
        license=openapi.License(name="BSD License"),
        ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path("architecture/", include("arch_works.urls")),
    path("my_works/", include("my_works.urls")),
    path("blog/", include("blog.urls")),
    path("contacts/", include("contact.urls")),
    path("news/", include("news.urls")),
    path('api/v1/', include('api.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('api/v1/dj-rest-auth/', include('dj_rest_auth.urls')),
    path('api/v1/dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    # Documentation(Swagger/Redoc)
    path('api-swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger'),
    path('api-redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)