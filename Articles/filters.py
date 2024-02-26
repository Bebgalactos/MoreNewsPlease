from django_filters import FilterSet , filters
from .models import Article

class ArticleFilters(FilterSet):
    author = filters.CharFilter(field_name="author",lookup_expr="icontains")
    title = filters.CharFilter(field_name="title",lookup_expr="icontains")

    class Meta: 
        model = Article
        fields = ["author","title"]