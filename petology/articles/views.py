from django.shortcuts import render
from django.views.generic import ListView
from .models import Article

class ArticleListView(ListView):
    model = Article
    template_name = 'articles/article_list.html'  # You need to create this template

