from django.urls import path
from .views import ArticleView, ChannelView

app_name = 'Articles'

urlpatterns = [
    path('articles/', view=ArticleView.as_view(), name="Articles"),
    path('articles/<uuid:id>',
         view=ArticleView.as_view(), name="ArticleDetail"),
    path('channels/', view=ChannelView.as_view(), name="Channels"),
    path('channels/<uuid:id>',
         view=ChannelView.as_view(), name="Channels")

]
