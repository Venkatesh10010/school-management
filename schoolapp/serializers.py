# serializers.py
from rest_framework import serializers
from .models import Student, Course, RankSheet


# Student Model Serializer
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
        # fields = ['id', 'name', 'dob', 'age', 'email', 'phone']


# Course Model Serializer
class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

    # Student + Course Model Serializer [in student model,for coming with course data]
class Student_Course_Serializer(serializers.ModelSerializer):
    courses = CourseSerializer(many=True)
    class Meta:
        model = Student
        fields = '__all__'

    # Course Model Serializer [in course model,coming student data instead of student id]
class Course_Data_Serializer(serializers.ModelSerializer):
    student = StudentSerializer()

    class Meta:
        model = Course
        fields = '__all__'
    #rank model serializer
class RankSheetSerializer(serializers.ModelSerializer):
    class Meta:
        model = RankSheet
        fields = ['id', 'sub1', 'sub2', 'sub3', 'sub4', 'sub5', 'total', 'average', 'result']
