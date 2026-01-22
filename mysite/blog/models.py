from django.db import models

# Create your models here.
from django.db import models

class Horse(models.Model):
    name = models.CharField(max_length=250)
    breed = models.CharField(max_length=100)
    origin = models.CharField(max_length=100)
    color = models.CharField(max_length=50)
    description = models.TextField()

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
