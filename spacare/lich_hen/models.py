from django.db import models
from django.utils.translation import gettext_lazy as _

from spacare.users.models import User
from spacare.uu_dai.models import UuDai


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
    thoi_gian_hen = models.DateTimeField()
    trang_thai = models.CharField(
        max_length=255, choices=TrangThai.choices, default=TrangThai.chua_duyet
    )
    uu_dai = models.ForeignKey(
        UuDai, null=True, on_delete=models.CASCADE, related_name="uu_dai"
    )
    tien_coc = models.BigIntegerField(null=True)
    tong_tien = models.BigIntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
