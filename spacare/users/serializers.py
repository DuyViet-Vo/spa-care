from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

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
        validators = [
            UniqueTogetherValidator(
                queryset=User.objects.all(),
                fields=["email"],
            ),
        ]


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
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


class UpdateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "quyen",
            "ho_ten",
            "sdt",
            "dia_chi",
            "ngay_sinh",
            "gioi_tinh",
            "trang_thai",
            "hinh_anh",
        )
