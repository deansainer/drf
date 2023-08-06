from django.db import models
from django.contrib.auth.models import User

class Nationality(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Nationalities'


class Person(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    nationality = models.ForeignKey(Nationality, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.name
