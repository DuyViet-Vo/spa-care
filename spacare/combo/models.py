from django.db import models

from spacare.danh_muc.models import DanhMuc


class Combo(models.Model):
    danh_muc = models.ForeignKey(
        DanhMuc, on_delete=models.CASCADE, related_name="danh_muc_combo"
    )
    ten_combo = models.CharField(max_length=255)
    hinh_anh = models.TextField(null=True)
    mo_ta = models.CharField(max_length=255)
    gia = models.BigIntegerField(null=True)
    selected = models.BooleanField(default=False, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
