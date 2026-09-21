from rest_framework.serializers import ModelSerializer

from consultor.models import Doubt


class DoubtSerializer(ModelSerializer):

    class Meta: 

        model = Doubt
        fields = [
            "id", 
            "mode", 
            "question", 
            "answer", 
            "created_at"
        ]
        read_only_fields = fields