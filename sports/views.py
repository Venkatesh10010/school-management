from django.shortcuts import render
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

# Create your views here.
from rest_framework.viewsets import ModelViewSet
from .models import Sport, Coach, Player
from .serializers import SportSerializer, CoachSerializer, PlayerSerializer
from django.core.cache import cache


class SportViewSet(ModelViewSet):
    queryset = Sport.objects.all()
    serializer_class = SportSerializer
    permission_classes = [AllowAny]

    def list(self, request, *args, **kwargs):
        data = cache.get("sports_list")

        if not data:
            print("CACHE MISS → DB HIT")   # FIRST TIME OR EXPIRED TIME
            response = super().list(request, *args, **kwargs)
            cache.set("sports_list", response.data, timeout=600)
            return response

        print("CACHE HIT → REDIS")         # CACHE WORKING
        return Response(data)


class CoachViewSet(ModelViewSet):
    queryset = Coach.objects.all()
    serializer_class = CoachSerializer

class PlayerViewSet(ModelViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
