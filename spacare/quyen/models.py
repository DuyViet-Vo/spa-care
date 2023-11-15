from django.db import models


class Quyen(models.Model):
    ten_quyen = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
