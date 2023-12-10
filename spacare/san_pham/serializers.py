from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from spacare.danh_muc.serializers import DanhMucSerializer
from spacare.san_pham.models import SanPham


class SanPhamSerializer(serializers.ModelSerializer):
    class Meta:
        model = SanPham
        fields = "__all__"
        extra_kwargs = {
            "id": {"read_only": True},
            "created_at": {"read_only": True},
            "updated_at": {"read_only": True},
        }
        validators = [
            UniqueTogetherValidator(
                queryset=SanPham.objects.all(),
                fields=["ten_san_pham"],
            ),
        ]


class ReadSanPhamSerializer(serializers.ModelSerializer):
    danh_muc = DanhMucSerializer(read_only=True)

    class Meta:
        model = SanPham
        fields = "__all__"
        extra_kwargs = {
            "id": {"read_only": True},
            "created_at": {"read_only": True},
            "updated_at": {"read_only": True},
        }
