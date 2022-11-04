from django.db import models

class Persondata(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name+': '+self.description