from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Breeds exist primarily for the Health Index - breed 
# impacts how many of which type of questions users will receive daily.
class Breed(models.Model):
    name = models.CharField(max_length=100)
    general_condition = models.IntegerField(default=1)  # Allmäntillstånd
    other = models.IntegerField(default=1)             # Övrigt
    dental_health = models.IntegerField(default=1)     # Munhälsa
    eyes = models.IntegerField(default=1)              # Ögon
    skin_and_coat = models.IntegerField(default=1)     # Hud och päls
    locomotor_system = models.IntegerField(default=1)  # Rörelseapparaten


    def __str__(self):
        return self.name



class Dog(models.Model):
    # SEX_CHOICES = (
    #     (1, 'Hane'),
    #     (2, 'Tik'),
    # )
    name = models.CharField(max_length=100)
    ownerId = models.ForeignKey(User, on_delete=models.CASCADE)
    breed = models.ForeignKey(Breed, on_delete=models.CASCADE)
    sex = models.CharField(max_length=100)
    birthday = models.DateField()

    # New fields
    pedigree_name = models.TextField(null=True, default=None)                 # Pedigree Name
    color = models.TextField(null=True, default=None)                         # Color
    insurance_company = models.TextField(null=True, default=None)             # Insurance Company
    insurance_number = models.TextField(null=True, default=None)              # Insurance Number
    feed = models.TextField(null=True, default=None)                          # Feed
    possible_feed_intolerance = models.TextField(null=True, default=None)     # Possible Feed Intolerance

    id_number = models.TextField(null=True, default=None)
    registration_number = models.TextField(null=True, default=None)
    passport_number = models.TextField(null=True, default=None)


    def __str__(self):
        return self.name


