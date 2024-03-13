from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from article.models import Article
from article.serializers import ArticleSerializer


@api_view(['POST'])
@permission_classes([AllowAny])
def get_articles(request):
    articles = Article.objects.filter(
        package_name=request.data['package_name']
    )
    if 'locale' in request.data:
        articles = articles.filter(locale=request.data['locale'])
    serializer = ArticleSerializer(articles, many=True)
    return Response(serializer.data)
