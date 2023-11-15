from django.contrib.auth.models import AbstractUser
from django.db import models

from spacare.quyen.models import Quyen

# Create your models here.


class User(AbstractUser):
    # Delete not use field
    username = None
    last_login = None
    is_staff = None
    is_superuser = (None,)
    first_name = (None,)
    last_name = (None,)

    password = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    quyen = models.ForeignKey(
        Quyen, on_delete=models.CASCADE, related_name="quyen_nguoi_dung"
    )
    ho_ten = models.CharField(max_length=255, null=True)
    sdt = models.CharField(max_length=10, null=True)
    dia_chi = models.CharField(max_length=255, null=True)
    ngay_sinh = models.DateField(blank=True, null=True)
    gioi_tinh = models.CharField(max_length=100, null=True)
    trang_thai = models.BooleanField(default=True)
    hinh_anh = models.CharField(max_length=255, null=True)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email
