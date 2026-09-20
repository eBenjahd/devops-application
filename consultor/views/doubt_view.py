from rest_framework.filters import SearchFilter
from rest_framework.generics import ListAPIView

from consultor.models import Doubt
from consultor.serializers import DoubtSerializer


class DoubtView(ListAPIView):
    
    serializer_class = DoubtSerializer
    filter_backends = [SearchFilter]
    # permission_classes = [IsAuthenticated] change in production 
    search_fields = ["question", "answer"]  

    def get_queryset(self):
        queryset = Doubt.objects.all()  # cambiar a filter(user=...) con JWT

        mode = self.request.query_params.get("mode") 
        if mode:
            queryset = queryset.filter(mode=mode)

        return queryset