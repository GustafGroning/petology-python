from django.db import models
from django.contrib.auth import get_user_model

from dogs.models import Dog
User = get_user_model()

class DogHealthIndex(models.Model):
    
    def __str__(self):
        return self.name

class HealthIndexQuestion(models.Model):
    
    def __str__(self):
        return self.name

class HealthIndexBatch(models.Model):

    def __str__(self):
        return self.name
