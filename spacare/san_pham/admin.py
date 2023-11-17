from django.contrib import admin

from spacare.san_pham.models import SanPham


@admin.register(SanPham)
class SanPhamAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "danh_muc",
        "hinh_anh",
        "ten_san_pham",
        "mo_ta",
        "gia",
        "so_luong",
        "created_at",
        "updated_at",
    )
