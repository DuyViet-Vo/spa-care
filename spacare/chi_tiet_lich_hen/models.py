from django.db import models

from spacare.dich_vu.models import DichVu
from spacare.lich_hen.models import LichHen


class ChiTietLichHen(models.Model):
    dich_vu = models.ForeignKey(
        DichVu, on_delete=models.CASCADE, related_name="chi_tiet_lich_hen_dich_vu"
    )
    lich_hen = models.ForeignKey(
        LichHen, on_delete=models.CASCADE, related_name="chi_tiet_lich_hen"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
