from rest_framework.serializers import ModelSerializer
from.models import *

class Book_Serializer(ModelSerializer):
    class Meta:
        model= Book
        fields="__all__"

class Laptop_Serializer(ModelSerializer):
    class Meta:
        model= Laptop
        fields="__all__"


#new course and student serailizers for M2M relationship

class CourseSerializer(ModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"


# New: Student serializer
class StudentSerializer(ModelSerializer):

    class Meta:
        model = Student
        fields = "__all__"