from django.db import models

# Create your models here.
class Book(models.Model):
    tittle=models.CharField(max_length=100)
    description=models.TextField()

class Laptop(models.Model):
    brand =models.CharField(max_length=100)
    model_name=models.CharField(max_length=100)
    user_type=models.CharField(max_length=100,null=True)


#many to many relationship
class Course(models.Model):
    name = models.CharField(max_length=120)
    description = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return f"{self.name} ({self.description})"


class Student(models.Model):
    name = models.CharField(max_length=120)
    roll_no = models.CharField(max_length=30, unique=True)

    # many-to-many to Course (child side)
    courses = models.ManyToManyField(Course, related_name='students', blank=True)

    def __str__(self):
        return f"{self.name} - {self.roll_no}"

