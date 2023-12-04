from django.contrib import admin

from spacare.lich_hen.models import LichHen


@admin.register(LichHen)
class LichHenAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "khach_hanh",
        "nhan_vien",
        "dich_vu",
        "thoi_gian_hen",
        "trang_thai",
        "created_at",
        "updated_at",
    )
