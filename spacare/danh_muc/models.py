from django.db import models


class DanhMuc(models.Model):
    ten_danh_muc = models.CharField(max_length=255)
    the_loai_danh_muc = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
