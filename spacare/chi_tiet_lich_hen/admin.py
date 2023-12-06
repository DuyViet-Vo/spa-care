from django.contrib import admin

from spacare.chi_tiet_lich_hen.models import ChiTietLichHen


@admin.register(ChiTietLichHen)
class ChiTietLichHenAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "dich_vu",
        "lich_hen",
        "created_at",
        "updated_at",
    )
