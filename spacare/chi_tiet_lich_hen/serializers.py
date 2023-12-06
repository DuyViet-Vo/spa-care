from rest_framework import serializers

from spacare.chi_tiet_lich_hen.models import ChiTietLichHen
from spacare.dich_vu.serializers import DichVuSerializer


class ChiTietLichHenSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChiTietLichHen
        fields = "__all__"
        extra_kwargs = {
            "id": {"read_only": True},
            "created_at": {"read_only": True},
            "updated_at": {"read_only": True},
        }


class ReadChiTietLichHenSerializer(serializers.ModelSerializer):
    dich_vu = DichVuSerializer(read_only=True)

    class Meta:
        model = ChiTietLichHen
        fields = "__all__"
        extra_kwargs = {
            "id": {"read_only": True},
            "created_at": {"read_only": True},
            "updated_at": {"read_only": True},
        }
