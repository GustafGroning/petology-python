from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Breeds exist primarily for the Health Index - breed 
# impacts how many of which type of questions users will receive daily.
class Breed(models.Model):
    name = models.CharField(max_length=100)
    # Add INT fields for handling health index stats. Will be used 
    # for randomizing daily questions.
    # Health index areas: 
        # Allmäntillstånd 
        # övrigt 
        # munhälsa 
        # ögon 
        # hud och päls 
        # rörelseapparaten


class Dog(models.Model):
    SEX_CHOICES = (
        (1, 'Hane'),  
        (2, 'Tik'),
    )
    name = models.CharField(max_length=100)
    ownerId = models.ForeignKey(User, on_delete=models.CASCADE)
    # breed = models.ForeignKey(Breed, on_delete=models.CASCADE)
    breed = models.CharField(max_length=100) # TODO: turn into list based on breeds in DB.
    sex = models.IntegerField(choices=SEX_CHOICES)
    birthday = models.DateField()

    def __str__(self):
        return self.name


