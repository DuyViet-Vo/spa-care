from django.contrib import admin

from spacare.dich_vu.models import DichVu


@admin.register(DichVu)
class DichVuAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "danh_muc",
        "hinh_anh",
        "ten_dich_vu",
        "mo_ta",
        "gia",
        "thoi_gian_thuc_hien",
        "created_at",
        "updated_at",
    )
