from django.db import models

class Persondata(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100, default='NOT SET')
    birthdate = models.CharField(max_length=100, default='NOT SET')
    
    def __str__(self):
        return 'Signature: ' + self.name + self.surname+ ' / Birthdate:' + self.birthdate