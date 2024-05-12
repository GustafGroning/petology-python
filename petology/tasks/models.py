from django.db import models
from dogs.models import Dog

class Task(models.Model):
    dog = models.ForeignKey(Dog, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=300, blank=True)
    start_time = models.DateField(null=True, blank=True)
    # end_time = models.DateTimeField(null=True, blank=True)
    repeat = models.IntegerField(blank=True, null=True)
    category = models.CharField(max_length=100, blank=True)
    reminder = models.CharField(max_length=100, blank=True)
    notes = models.TextField(blank=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    

    @property
    def dog_name(self):
        return self.dog.name if self.dog else None
