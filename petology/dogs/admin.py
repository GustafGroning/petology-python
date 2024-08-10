from django.contrib import admin
from .models import Dog, Breed
from tasks.models import Task
from articles.models import Article
from health_index.models import HealthIndexBatch, HealthIndexQuestion, DogHealthIndex, Toothbrushing
from health_records.models import Medication, Condition, Vaccination
# Register your models here.

admin.site.register(Task)
admin.site.register(Dog)
admin.site.register(Breed)
admin.site.register(DogHealthIndex)
admin.site.register(HealthIndexBatch)
admin.site.register(HealthIndexQuestion)
admin.site.register(Toothbrushing)

admin.site.register(Medication)
admin.site.register(Condition)
admin.site.register(Vaccination)
# admin.site.register(Article)