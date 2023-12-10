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

from spacare.chi_tiet_lich_hen.views import (
    BulkCreateChiTietLichHenView,
    ListCreateChiTietLichHenView,
    UpdateDeleteChiTietLichHenView,
)
from spacare.danh_muc.views import ListCreateDanhMucView, UpdateDeleteDanhMucView
from spacare.dich_vu.views import ListCreateDichVuView, UpdateDeleteDichVuView
from spacare.lich_hen.views import ListCreateLichHenView, UpdateDeleteLichHenView
from spacare.quyen.views import ListCreateQuyenView, UpdateDeleteQuyenView
from spacare.san_pham.views import ListCreateSanPhamView, UpdateDeleteSanPhamView
from spacare.users.views import (
    ListNhanVienView,
    ListUserView,
    UpdateUserView,
    UserRegisterView,
    UserView,
)

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
    path("api/user", UserView.as_view()),
    path("api/user/<str:id>", UpdateUserView.as_view()),
    path("api/nhan-vien", ListNhanVienView.as_view()),
    path("api/list-user", ListUserView.as_view()),
    # Quyen
    path("api/quyen", ListCreateQuyenView.as_view()),
    path("api/quyen/<str:id>", UpdateDeleteQuyenView.as_view()),
    # Danh Muc
    path("api/danh-muc", ListCreateDanhMucView.as_view()),
    path("api/danh-muc/<str:id>", UpdateDeleteDanhMucView.as_view()),
    # San Pham
    path("api/san-pham", ListCreateSanPhamView.as_view()),
    path("api/san-pham/<str:id>", UpdateDeleteSanPhamView.as_view()),
    # Dich Vu
    path("api/dich-vu", ListCreateDichVuView.as_view()),
    path("api/dich-vu/<str:id>", UpdateDeleteDichVuView.as_view()),
    # lich hen
    path("api/lich-hen", ListCreateLichHenView.as_view()),
    path("api/lich-hen/<str:id>", UpdateDeleteLichHenView.as_view()),
    # Chi tiet lich hen
    path("api/chi-tiet-lich-hen/bulk", BulkCreateChiTietLichHenView.as_view()),
    path("api/chi-tiet-lich-hen", ListCreateChiTietLichHenView.as_view()),
    path("api/chi-tiet-lich-hen/<str:id>", UpdateDeleteChiTietLichHenView.as_view()),
]
