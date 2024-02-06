from django.urls import path
from .views import ArticleListView, get_article_by_id

urlpatterns = [
    path('', ArticleListView.as_view(), name='article-list'),
    path('get/<int:article_id>/', get_article_by_id, name='article-detail'),



    # You can add more URL patterns as needed
]
