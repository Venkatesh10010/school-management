# sports/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SportViewSet, CoachViewSet, PlayerViewSet

router = DefaultRouter()
router.register(r'sports', SportViewSet, basename='sport')
router.register(r'coaches', CoachViewSet, basename='coach')
router.register(r'players', PlayerViewSet, basename='player')

urlpatterns = [
    path('', include(router.urls)),
]
