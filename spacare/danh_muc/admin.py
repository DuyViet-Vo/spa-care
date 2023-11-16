from django.contrib import admin

from spacare.danh_muc.models import DanhMuc


@admin.register(DanhMuc)
class DanhMucAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "ten_danh_muc",
        "the_loai_danh_muc",
        "created_at",
        "updated_at",
    )
