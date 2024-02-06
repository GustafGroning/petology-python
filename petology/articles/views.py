from rest_framework.generics import ListAPIView
from .models import Article
from .serializers import ArticleListSerializer, ArticleDetailSerializer
from rest_framework.generics import RetrieveAPIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

class ArticleListView(ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleListSerializer


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_article_by_id(request, article_id):
    try:
        print('we are getting articlez')
        article = Article.objects.get(id=article_id)
    except Article.DoesNotExist:
        return Response({'error': 'Article not found'}, status=404)

    serializer = ArticleDetailSerializer(article)
    return Response(serializer.data, status=200)
    
# @api_view(['GET'])
# @permission_classes([IsAuthenticated])
# def get_article_by_id(request, article_id):
#     article = get_object_or_404(Article, id=article_id)
#     print('article based on ', article_id, ' ', article)