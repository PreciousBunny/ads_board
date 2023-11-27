from django.urls import path, include
from rest_framework_nested import routers
from rest_framework.routers import SimpleRouter

from ads.apps import SalesConfig
from ads.views import AdViewSet, CommentViewSet

ads_router = SimpleRouter()
ads_router.register(r"ads", AdViewSet, basename="ads")
comments_router = routers.NestedSimpleRouter(ads_router, "ads", lookup="ad")
comments_router.register(r"comments", CommentViewSet, basename="comments")

app_name = SalesConfig.name

# TODO настройка роутов для модели


urlpatterns = [
    path('', include(ads_router.urls)),
    path('', include(comments_router.urls)),
]
