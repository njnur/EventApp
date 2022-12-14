from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny


class HomeView(APIView):
    permission_classes = [AllowAny]

    @staticmethod
    def get(request):
        return Response({
            'message': 'Welcome to EventApp!!'
        },
            status=status.HTTP_200_OK
        )


class PingTestView(APIView):
    permission_classes = [AllowAny]

    @staticmethod
    def get(request):
        return Response({
            'message': 'Pong!!'
        },
            status=status.HTTP_200_OK
        )
