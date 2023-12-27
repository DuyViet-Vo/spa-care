from rest_framework import serializers


class EmailSend(serializers.Serializer):
    to_email = serializers.CharField()
