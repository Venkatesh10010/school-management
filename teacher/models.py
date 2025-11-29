# Create your models here.
from django.db import models

class Teacher(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(null=True, blank=True)
    email = models.EmailField(unique=True, null=True, blank=True)
    phone = models.CharField(max_length=15, null=True, blank=True)

    def __str__(self):
        return f"{self.name} ({self.age})"

class Subject(models.Model):
    subject_name = models.CharField(max_length=100)
    code = models.CharField(max_length=20, unique=True, null=True, blank=True)

    def __str__(self):
        return self.subject_name


class Classroom(models.Model):
    room_no = models.CharField(max_length=10, unique=True)
    floor = models.IntegerField(null=True, blank=True)
    capacity = models.IntegerField(null=True, blank=True)

    # ForeignKey to Subject
    subject = models.ForeignKey(
        'Subject',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='classrooms'
    )

    def __str__(self):
        return f"Room {self.room_no}"

class TeacherDetail(models.Model):
    teacher = models.OneToOneField(Teacher, on_delete=models.CASCADE, related_name='details')
    qualification = models.CharField(max_length=200, null=True, blank=True)
    experience = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.teacher.name} Details"
