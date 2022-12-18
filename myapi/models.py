from django.db import models

#import numerology
# import myapi.srcs.numerology as numrl

def ret_numerology(name, surname, date):
    
    return 'numerology'

class Persondata(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100, default='NOT SET')
    date = models.CharField(max_length=100, default='NOT SET')
    numerology = models.CharField(max_length=100, default=ret_numerology(name, surname, date))
    
    def __str__(self):
        return  self.name + ' ' + self.surname + '. Birthdate: ' + self.date + 'numerology:'
    