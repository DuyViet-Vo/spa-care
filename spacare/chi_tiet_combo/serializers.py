from rest_framework import serializers

from spacare.chi_tiet_combo.models import ChiTietCombo


class ChiTietComboSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChiTietCombo
        fields = "__all__"
        extra_kwargs = {
            "id": {"read_only": True},
            "created_at": {"read_only": True},
            "updated_at": {"read_only": True},
        }
