"""
URL configuration for MoreNewsPlease project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from accounts import urls as accounts_urls
from Articles.views import CategoryViewset, NewspaperViewset, ArticleViewset
from Interactions.views import InteractionsViewset , HistoryViewset
from recommendations.views import RecommendationViewSet
from drf_spectacular.views import SpectacularSwaggerView, SpectacularAPIView
from rest_framework_nested import routers
router = routers.DefaultRouter()
router.register(r'articles', ArticleViewset, basename="article")
router.register(r'newspapers', NewspaperViewset, basename='newspaper')
router.register(r'history', HistoryViewset, basename='history')
router.register(r'categories', CategoryViewset, basename='category')
router.register(r'recommendations',RecommendationViewSet, basename='recommendation')
interactions_routers = routers.NestedDefaultRouter(router, r'articles', lookup='article')
interactions_routers.register(r'interactions',InteractionsViewset,basename= 'interaction')
urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include((accounts_urls, 'accounts'))),
    path('api/', include(router.urls)),
    path('api/', include(interactions_routers.urls)),
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "docs/",
        SpectacularSwaggerView.as_view(
            template_name="swagger-ui.html", url_name="schema"
        ),
        name="MoreNewsPlease API",
    ),
]
