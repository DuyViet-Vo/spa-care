from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from spacare.chi_tiet_combo.serializers import ChiTietComboSerializer
from spacare.combo.models import Combo


class ComboSerializer(serializers.ModelSerializer):
    class Meta:
        model = Combo
        fields = "__all__"
        extra_kwargs = {
            "id": {"read_only": True},
            "created_at": {"read_only": True},
            "updated_at": {"read_only": True},
        }
        validators = [
            UniqueTogetherValidator(
                queryset=Combo.objects.all(),
                fields=["ten_combo"],
            ),
        ]


class ReadComboSerializer(serializers.ModelSerializer):
    chi_tiet_combo = ChiTietComboSerializer(many=True, read_only=True)

    class Meta:
        model = Combo
        fields = "__all__"
        extra_kwargs = {
            "id": {"read_only": True},
            "created_at": {"read_only": True},
            "updated_at": {"read_only": True},
        }
