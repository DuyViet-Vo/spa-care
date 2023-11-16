"""spacare URL Configuration

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
from django.contrib import admin
from django.urls import path, re_path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework_simplejwt import views as jwt_views

from spacare.danh_muc.views import ListCreateDanhMucView, UpdateDeleteDanhMucView
from spacare.quyen.views import ListCreateQuyenView, UpdateDeleteQuyenView
from spacare.users.views import UserRegisterView

schema_view = get_schema_view(
    openapi.Info(
        title="Spa-Care",
        default_version="v1",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    url=settings.HOST + "api/",
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    re_path(
        r"^docs/$",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path("admin/", admin.site.urls),
    # User
    path("api/register", UserRegisterView.as_view(), name="register"),
    path("api/login", jwt_views.TokenObtainPairView.as_view(), name="login"),
    # Quyen
    path("api/quyen", ListCreateQuyenView.as_view()),
    path("api/quyen/<str:id>", UpdateDeleteQuyenView.as_view()),
    # Danh Muc
    path("api/danh-muc", ListCreateDanhMucView.as_view()),
    path("api/danh-muc/<str:id>", UpdateDeleteDanhMucView.as_view()),
]
