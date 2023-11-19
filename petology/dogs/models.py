from django.db import models

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
    name = models.CharField(max_length=100)

    # Foreign keys
    breed = models.ForeignKey(Breed, on_delete=models.CASCADE)



