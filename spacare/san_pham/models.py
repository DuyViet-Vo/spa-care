from django.db import models

from spacare.danh_muc.models import DanhMuc


class SanPham(models.Model):
    danh_muc = models.ForeignKey(DanhMuc, on_delete=models.CASCADE)
    hinh_anh = models.TextField(null=True)
    ten_san_pham = models.CharField(max_length=255)
    mo_ta = models.CharField(max_length=255, null=True)
    gia = models.BigIntegerField(default=0)
    so_luong = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
