from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import  TeacherDetailViewSet, TeacherViewSet

router = DefaultRouter()
router.register(r'teacher-model', TeacherDetailViewSet, basename='teachermodel')

router.register(r'signals', TeacherViewSet, basename='teachers')           # POST /teacher/signals/


urlpatterns = [
    # your existing API (keep as-is)
    # path('details/', TeacherAPI.as_view(), name='teacher-details'),

    # router URLs for ModelViewSet
    path('', include(router.urls)),
]
