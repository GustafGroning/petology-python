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
class DogHealthIndex(models.Model):
    dog = models.ForeignKey(Dog, on_delete=models.CASCADE)
    latest_run_batch_id = models.IntegerField(default=1)
    batches_in_row = models.IntegerField(default=0)
    date_performed = models.DateTimeField()
    general_condition = models.IntegerField(default=1)  # Allmäntillstånd
    dental_health = models.IntegerField(default=1)      # Munhälsa
    eyes = models.IntegerField(default=1)               # Ögon
    skin_and_coat = models.IntegerField(default=1)      # Hud och päls
    locomotor_system = models.IntegerField(default=1)   # Rörelseapparaten
    other = models.IntegerField(default=1)              # Övrigt

    # Is the only point of this what appears in the admin view list?
    def __str__(self):
        return f'{self.dog} {self.date_performed}'


"""
The questions that actually makes up a batch.
Included a JSON-field with all possible answers and their values.
"""
class HealthIndexQuestion(models.Model):
    question_title = models.CharField(max_length=250)
    responses = models.JSONField()


    def __str__(self):
        return f'Question {self.id}'


FREQUENCY_CHOICES = (
    (1, '7/week'),
    (2, '3/week'),
    (3, 'Custom'), # Use custom later for any dogs where user sets a custom time span.
)
class HealthIndexBatch(models.Model):
    questions = models.JSONField() # JSON-structure with question IDs
    frequency = models.IntegerField( choices=FREQUENCY_CHOICES, default=1)

    # def __str__(self):
    #     return self.questions
