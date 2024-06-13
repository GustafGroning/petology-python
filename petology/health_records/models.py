from django.db import models
from django.contrib.auth import get_user_model

from dogs.models import Dog
User = get_user_model()

"""
Each row is on HealthIndex entry for a dog.
Keeps track of the dogs current score in each category, as
well as the latest run batch. 
Can get historical data by bringing out all rows for a dog, or get present
data by filtering for latest row only.
"""


class Medication(models.Model):
    name = models.CharField(max_length=120, null=False)
    strength = models.CharField(max_length=120, null=False)
    administration_method = models.CharField(max_length=120, null=False)
    amount = models.CharField(max_length=120, null=False)
    frequency = models.CharField(max_length=120, null=False)
    administration_start_date = models.DateField(null=False)

    # Users will be offered 2 dropdowns, chosing an INT and "day/week/month".
    # This will then be parsed into a normal date, starting from administration_start_date.
    administration_length = models.DateField(null=False)
    

    def __str__(self):
        return self

class Condition(models.Model):
    dog = models.ForeignKey(Dog, on_delete=models.CASCADE)
    name = models.CharField(max_length=120, null=False)
    onset_date = models.DateField()
    follow_up_date = models.DateField()
    vet_clinic = models.CharField(max_length=120, null=True)
    notes = models.CharField(max_length=120)

    # This should maybe NOT cascade?
    medication = models.ForeignKey(Medication, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self

class Vaccination(models.Model):
    dog = models.ForeignKey(Dog, on_delete=models.CASCADE)
    name = models.CharField(max_length=120)
    vaccination_date = models.DateField()
    next_vaccination_date = models.DateField(null=True)
    clinic_name = models.CharField(max_length=120)
    notes = models.CharField(max_length=120)

    def __str__(self):
        return f'{self.dog} - {self.name}'
