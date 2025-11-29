from rest_framework.routers import DefaultRouter
from.views import BookView,CourseView, StudentView

library_router=DefaultRouter()
library_router.register(r'book',BookView)
library_router.register(r'course', CourseView, basename='course')
library_router.register(r'student', StudentView, basename='student')