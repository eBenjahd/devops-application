from openai import OpenAIError
from rest_framework import status
from rest_framework.response import Response

from adrf.views import APIView
from consultor.models import Doubt
from consultor.serializers import AskSerializer
from consultor.services import CallAIModel, UNKNOWN 


class AskView(APIView):

    async def post(self, request):

        serializer = AskSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data

        ask_ai = CallAIModel(model="gpt-4.1-mini-2025-04-14")

        try:
            answer = await ask_ai.call_open_ai(
                data["message"],
                data["mode"],
            )

        except OpenAIError:

            return Response(
                {"error": "El servicio de IA no está disponible, intenta de nuevo."},
                status=status.HTTP_502_BAD_GATEWAY,
            )
        
        if answer.strip().strip(".").upper() == UNKNOWN:
            
            return Response(
                {"error": "No puedo ayudarte con eso. Solo respondo consultas de DevOps."},
                status=status.HTTP_422_UNPROCESSABLE_ENTITY,
            )

        consulta = await Doubt.objects.acreate(

            user=(
                request.user
                if request.user.is_authenticated
                else None
            ),
            mode=data["mode"],
            question=data["message"],
            answer=answer,
        )

        return Response(
            {
                "id": consulta.id,
                "answer": answer,
            },
            status=status.HTTP_201_CREATED,
        )