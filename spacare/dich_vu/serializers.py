from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from spacare.danh_muc.serializers import DanhMucSerializer
from spacare.dich_vu.models import DichVu


class DichVuSerializer(serializers.ModelSerializer):
    class Meta:
        model = DichVu
        fields = "__all__"
        extra_kwargs = {
            "id": {"read_only": True},
            "created_at": {"read_only": True},
            "updated_at": {"read_only": True},
        }
        validators = [
            UniqueTogetherValidator(
                queryset=DichVu.objects.all(),
                fields=["ten_dich_vu"],
            ),
        ]


class ReadDichVuSerializer(serializers.ModelSerializer):
    danh_muc = DanhMucSerializer(read_only=True)

    class Meta:
        model = DichVu
        fields = "__all__"
        extra_kwargs = {
            "id": {"read_only": True},
            "created_at": {"read_only": True},
            "updated_at": {"read_only": True},
        }
