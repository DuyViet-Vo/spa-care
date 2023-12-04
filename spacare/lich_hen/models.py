from django.db import models
from django.utils.translation import gettext_lazy as _

from spacare.dich_vu.models import DichVu
from spacare.users.models import User


class TrangThai(models.TextChoices):
    chua_duyet = "Chưa Duyệt", _("chua_duyet")
    da_duyet = "Đã Duyệt", _("da_duyet")


class LichHen(models.Model):
    khach_hanh = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="khach_hang"
    )
    nhan_vien = models.ForeignKey(
        User, null=True, on_delete=models.CASCADE, related_name="nhan_vien"
    )
    dich_vu = models.ForeignKey(DichVu, on_delete=models.CASCADE)
    thoi_gian_hen = models.DateTimeField()
    trang_thai = models.CharField(
        max_length=255, choices=TrangThai.choices, default=TrangThai.chua_duyet
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
