from rest_framework import serializers

from spacare.uu_dai.models import UuDai


class UuDaiSerializer(serializers.ModelSerializer):
    class Meta:
        model = UuDai
        fields = "__all__"
        extra_kwargs = {
            "id": {"read_only": True},
            "created_at": {"read_only": True},
            "updated_at": {"read_only": True},
        }
