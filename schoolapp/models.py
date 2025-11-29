from django.db import models

# Create your models here.

# Student Model
class Student(models.Model):
    name = models.CharField(max_length=100)
    dob = models.DateField(null=True, blank=True)   # Date of Birth
    age = models.IntegerField(null=True, blank=True)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, null=True, blank=True)

    def __str__(self):
        return f"{self.name} ({self.email})"

class Course(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='courses', null=True, blank=True)
    course_name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.course_name


class RankSheet(models.Model):
    sub1 = models.IntegerField()
    sub2 = models.IntegerField()
    sub3 = models.IntegerField()
    sub4 = models.IntegerField()
    sub5 = models.IntegerField()
    total = models.IntegerField()
    average = models.FloatField()
    result = models.BooleanField()