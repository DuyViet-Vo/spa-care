from rest_framework import serializers

from spacare.users.models import User


class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "password",
            "email",
            "quyen",
            "ho_ten",
            "sdt",
            "dia_chi",
            "ngay_sinh",
            "gioi_tinh",
            "trang_thai",
            "hinh_anh",
        )
        extra_kwargs = {"password": {"write_only": True}}
