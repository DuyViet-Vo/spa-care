from rest_framework import serializers

from spacare.chi_tiet_lich_hen.models import ChiTietLichHen
from spacare.dich_vu.serializers import DichVuSerializer
from spacare.lich_hen.models import LichHen


class ChiTietLichHenSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChiTietLichHen
        fields = "__all__"
        extra_kwargs = {
            "id": {"read_only": True},
            "created_at": {"read_only": True},
            "updated_at": {"read_only": True},
        }


class LichHenSerializerShow(serializers.ModelSerializer):
    class Meta:
        model = LichHen
        fields = "__all__"
        extra_kwargs = {
            "id": {"read_only": True},
            "created_at": {"read_only": True},
            "updated_at": {"read_only": True},
        }


class ReadChiTietLichHenSerializer(serializers.ModelSerializer):
    dich_vu = DichVuSerializer(read_only=True)
    lich_hen = LichHenSerializerShow(read_only=True)

    class Meta:
        model = ChiTietLichHen
        fields = "__all__"
        extra_kwargs = {
            "id": {"read_only": True},
            "created_at": {"read_only": True},
            "updated_at": {"read_only": True},
        }


class BulkChiTietLichHenSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChiTietLichHen
        fields = [
            "dich_vu",
            "lich_hen",
            "trang_thai",
        ]
