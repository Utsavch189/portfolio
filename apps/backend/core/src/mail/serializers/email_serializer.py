from rest_framework import serializers
from src.mail.models import Email
from benedict import benedict

class EmailSerializerForOutput(serializers.ModelSerializer):

    class Meta:
        model=Email
        fields='__all__'


class EmailSerializerForInput(serializers.Serializer):

    sent_mail=serializers.EmailField()
    subject=serializers.CharField()
    body=serializers.CharField()

    def validate(self, data):
        return benedict(data)