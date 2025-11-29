from django.db import models


class Sport(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=255, blank=True)  # second field

    def __str__(self):
        return self.name


class Coach(models.Model):
    sport = models.ForeignKey(Sport, related_name="coaches", on_delete=models.CASCADE)
    name = models.CharField(max_length=120)
    contact = models.CharField(max_length=50, blank=True)  # phone or email

    def __str__(self):
        return f"{self.name} ({self.sport.name})"


class Player(models.Model):
    # link to your school.Student model (optional=False -> must link)
    student = models.ForeignKey('schoolapp.Student',on_delete=models.CASCADE,related_name='sports_profiles')
    sport = models.ForeignKey(Sport, related_name='players', on_delete=models.CASCADE)
    jersey_number = models.PositiveIntegerField(null=True, blank=True)  # field 1

    def __str__(self):
        return f"{self.student} - {self.sport.name}"
