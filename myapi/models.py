from django.db import models

class Persondata(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100, default='NOT SET')
    date = models.CharField(max_length=100, default='NOT SET')
    
    def __str__(self):
        return  self.name + ' ' + self.surname + '. Birthdate: ' + self.date
    
class PersonNumerology(models.Model):
    # Foreign means that this is a foreign key referring to Persondata
    # On_delete=models.CASCADE means that if the person is deleted, the numerology is deleted too
    person = models.ForeignKey(Persondata, on_delete=models.CASCADE)
    numerology = models.CharField(max_length=100, default='NOT SET')
    
    def __str__(self):
        return  self.person.name + ' ' + self.person.surname + '. Numerology: ' + self.numerology