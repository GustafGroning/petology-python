from django.contrib import admin
from .models import Dog, Breed
from tasks.models import Task
from articles.models import Article

# Register your models here.

admin.site.register(Task)
admin.site.register(Dog)
admin.site.register(Breed)
# admin.site.register(Article)