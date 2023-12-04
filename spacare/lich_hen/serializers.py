from rest_framework import serializers

from spacare.dich_vu.serializers import DichVuSerializer
from spacare.lich_hen.models import LichHen
from spacare.users.serializers import UserSerializer


class LichHenSerializer(serializers.ModelSerializer):
    class Meta:
        model = LichHen
        fields = "__all__"
        extra_kwargs = {
            "id": {"read_only": True},
            "created_at": {"read_only": True},
            "updated_at": {"read_only": True},
        }


class ReadLichHenSerializer(serializers.ModelSerializer):
    khach_hanh = UserSerializer(read_only=True)
    nhan_vien = UserSerializer(read_only=True)
    dich_vu = DichVuSerializer(read_only=True)

    class Meta:
        model = LichHen
        fields = "__all__"
        extra_kwargs = {
            "id": {"read_only": True},
            "created_at": {"read_only": True},
            "updated_at": {"read_only": True},
        }
