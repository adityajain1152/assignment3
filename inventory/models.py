from django.db import models
from django.urls import reverse

class Machine(models.Model):

    Name = models.CharField(max_length=100)
    Description = models.CharField(max_length=500)
    Availability = models.BooleanField()
    Price = models.IntegerField()

    def get_absolute_url(self):
        return reverse("index")
    

    def __str__(self):
       return self.Name