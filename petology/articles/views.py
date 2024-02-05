from rest_framework.generics import ListAPIView
from .models import Article
from .serializers import ArticleListSerializer

class ArticleListView(ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleListSerializer
