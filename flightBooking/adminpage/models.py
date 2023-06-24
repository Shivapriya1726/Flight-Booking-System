from django.db import models

# Create your models here.
from django.db import models

class Flight(models.Model):
    name = models.CharField(max_length=100)
    flight_number = models.CharField(max_length=20)
    time = models.DateTimeField()

    def __str__(self):
        return self.name