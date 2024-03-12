from django_filters import FilterSet, filters
from .models import Article


class ArticleFilters(FilterSet):
    author = filters.CharFilter(field_name="author", lookup_expr="icontains")
    title = filters.CharFilter(field_name="title", lookup_expr="icontains")
    publication_date = filters.DateFilter(field_name="publication_date")
    newspaper = filters.CharFilter(field_name="newspaper_id", lookup_expr="exact")
    favorite_only = filters.BooleanFilter(method="filter_favorite_only")

    class Meta:
        model = Article
        fields = ["author", "title", "publication_date", "newspaper"]

    def filter_favorite_only(self, queryset, name, value):
        if value:
            return queryset.filter(
                article_interactions__interaction_type="favorite",
                article_interactions__user=self.request.user,
            )
        return queryset
