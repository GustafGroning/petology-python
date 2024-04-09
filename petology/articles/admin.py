from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Article

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'publication_date', 'summary')
    search_fields = ('title', 'summary')
    list_filter = ('publication_date',)
