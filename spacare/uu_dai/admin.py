from django.contrib import admin

from spacare.uu_dai.models import UuDai


@admin.register(UuDai)
class UuDaiAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "ma_uu_dai",
        "phan_tram",
        "created_at",
        "updated_at",
    )
