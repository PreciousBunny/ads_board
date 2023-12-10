from django.urls import include, path
from djoser.views import UserViewSet
from rest_framework.routers import DefaultRouter

from users.apps import UsersConfig

# подключите UserViewSet из Djoser.views к нашим urls.py
# для этокого рекоммендуется использовать SimpleRouter

user_router = DefaultRouter()
user_router.register(r'users', UserViewSet, basename='users')

app_name = UsersConfig.name

urlpatterns = [
    path('', include(user_router.urls)),
]
