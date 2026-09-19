from rest_framework import serializers
from consultor.models import Doubt


class AskSerializer(serializers.Serializer):

    message = serializers.CharField(max_length=2000)
    mode = serializers.ChoiceField(
        choices=Doubt.Mode.choices, default=Doubt.Mode.CONSULTOR
    )