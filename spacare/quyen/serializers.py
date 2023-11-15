from rest_framework import serializers

from spacare.quyen.models import Quyen


class QuyenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quyen
        fields = "__all__"
        extra_kwargs = {
            "id": {"read_only": True},
            "created_at": {"read_only": True},
            "updated_at": {"read_only": True},
        }
