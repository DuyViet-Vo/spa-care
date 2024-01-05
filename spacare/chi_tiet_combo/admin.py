from django.contrib import admin

from spacare.chi_tiet_combo.models import ChiTietCombo


@admin.register(ChiTietCombo)
class ChiTietComboAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "combo",
        "dich_vu",
        "created_at",
        "updated_at",
    )
