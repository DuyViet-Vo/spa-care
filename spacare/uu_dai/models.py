from django.db import models


class UuDai(models.Model):
    ma_uu_dai = models.CharField(max_length=255)
    phan_tram = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
