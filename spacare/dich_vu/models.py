from django.db import models

from spacare.danh_muc.models import DanhMuc


class DichVu(models.Model):
    danh_muc = models.ForeignKey(DanhMuc, on_delete=models.CASCADE)
    hinh_anh = models.CharField(max_length=255, null=True)
    ten_dich_vu = models.CharField(max_length=255)
    mo_ta = models.CharField(max_length=255, null=True)
    gia = models.BigIntegerField(default=0)
    thoi_gian_thuc_hien = models.IntegerField(default=0, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
