from rest_framework.permissions import BasePermission
from users.models import UserRoles


# здесь производится настройка пермишенов для нашего проекта

class AdminOrOwner(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        return request.user.role == UserRoles.ADMIN or obj.author == request.user
