from django.db import models

from spacare.combo.models import Combo
from spacare.dich_vu.models import DichVu


class ChiTietCombo(models.Model):
    combo = models.ForeignKey(
        Combo, on_delete=models.CASCADE, related_name="chi_tiet_combo"
    )
    dich_vu = models.ForeignKey(
        DichVu, on_delete=models.CASCADE, related_name="combo_dich_vu"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
