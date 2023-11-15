from django.contrib import admin

from spacare.quyen.models import Quyen


@admin.register(Quyen)
class QuyenAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "ten_quyen",
        "created_at",
        "updated_at",
    )
