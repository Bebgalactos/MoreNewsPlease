from django.urls import path , include
from .views import NewspaperViewset , ArticleViewset
from rest_framework.routers import DefaultRouter
app_name = 'Articles'
router = DefaultRouter()
router.register(r'newspapers', NewspaperViewset, "Newspapers")
router.register(r'articles',ArticleViewset, "Articles")

urlpatterns = [
    path('', include(router.urls)),
]
