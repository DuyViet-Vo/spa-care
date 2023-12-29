from rest_framework import serializers


class SendEmailLichHen(serializers.Serializer):
    id_lich_hen = serializers.IntegerField()
