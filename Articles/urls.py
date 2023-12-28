from django.urls import path
from .views import ArticleView

app_name = 'Articles'

urlpatterns = [
    path('articles/', view=ArticleView.as_view(), name="Articles"),
    path('articles/<uuid:id>',
         view=ArticleView.as_view(), name="ArticleDetail")

]
