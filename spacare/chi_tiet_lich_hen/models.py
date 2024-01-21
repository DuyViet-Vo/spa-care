from django.db import models
from django.utils.translation import gettext_lazy as _

from spacare.dich_vu.models import DichVu
from spacare.lich_hen.models import LichHen
from spacare.users.models import User


class TrangThai(models.TextChoices):
    chua_thuc_hien = "Chưa Thực Hiện", _("chua_thuc_hien")
    dang_thuc_hien = "Đang Thực Hiện", _("dang_thuc_hien")
    da_hoan_thanh = "Đã hoàn thành", _("da_hoan_thanh")


class ChiTietLichHen(models.Model):
    nhan_vien = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="nhan_vien_lam", null=True
    )
    dich_vu = models.ForeignKey(
        DichVu, on_delete=models.CASCADE, related_name="chi_tiet_lich_hen_dich_vu"
    )
    lich_hen = models.ForeignKey(
        LichHen, on_delete=models.CASCADE, related_name="chi_tiet_lich_hen"
    )
    trang_thai = models.CharField(
        max_length=255, choices=TrangThai.choices, default=TrangThai.chua_thuc_hien
    )
    ghi_chu = models.CharField(null=True, max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
