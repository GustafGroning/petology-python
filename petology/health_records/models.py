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

class Condition(models.Model):
    dog = models.ForeignKey(Dog, on_delete=models.CASCADE)
    name = models.CharField(max_length=120, null=False)
    onset_date = models.DateField()
    follow_up_date = models.DateField(null=True)
    healed = models.BooleanField(default=False)
    vet_clinic = models.CharField(max_length=120, null=True, blank=True)
    notes = models.CharField(max_length=120, null=True, blank=True)

    def __str__(self):
        return f'{self.dog} - {self.name}'

class Medication(models.Model):
    name = models.CharField(max_length=120, null=False)
    strength = models.CharField(max_length=120, null=False)
    administration_method = models.CharField(max_length=120, null=False)
    amount = models.CharField(max_length=120, null=False)
    frequency = models.CharField(max_length=120, null=False)
    administration_start_date = models.DateField(null=False)

    administration_length = models.DateField(null=False)
    dog = models.ForeignKey(Dog, null=True, blank=True, on_delete=models.CASCADE)
    condition = models.ForeignKey(Condition, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.id} - {self.name}'

class Vaccination(models.Model):
    dog = models.ForeignKey(Dog, on_delete=models.CASCADE)
    name = models.CharField(max_length=120)
    vaccination_detailed_name = models.CharField(max_length=120, null=True)
    vaccination_date = models.DateField()
    next_vaccination_date = models.DateField(null=True)
    clinic_name = models.CharField(max_length=120, null=True)
    notes = models.CharField(max_length=120, null=True, blank=True)

    def __str__(self):
        return f'{self.dog} - {self.name}'
