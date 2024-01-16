from django.contrib import admin

from spacare.combo.models import Combo


@admin.register(Combo)
class ComboAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "danh_muc",
        "ten_combo",
        "mo_ta",
        "gia",
        "created_at",
        "updated_at",
    )
