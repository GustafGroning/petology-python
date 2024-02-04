from django.urls import path
from .views import ArticleListView

urlpatterns = [
    path('', ArticleListView.as_view(), name='article-list'),
    # You can add more URL patterns as needed
]
