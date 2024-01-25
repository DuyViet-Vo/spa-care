from rest_framework import serializers


class SendEmailLichHen(serializers.Serializer):
    id_lich_hen = serializers.IntegerField()


class SendEmialChiTiet(serializers.Serializer):
    id_chi_tiet = serializers.IntegerField()
