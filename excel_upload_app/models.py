from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.TextField(max_length=50)
    blood_type = models.TextField(max_length=40)
    age = models.IntegerField()
    date_of_birth = models.DateField(null=True)
    
    # to String
    def __str__(self):
        return self.name


