from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from users.models import User
from users.serializers import CurrentUserSerializer, UserRegistrationSerializer


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = CurrentUserSerializer
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        if self.action == 'me':
            return User.objects.get(id=self.request.user.id)
        return User.objects.all()

    def get_serializer_class(self):
        if self.action == "create":
            return UserRegistrationSerializer
        return CurrentUserSerializer

    @action(("get", "put", "patch", "delete",), detail=False)
    def me(self, request, *args, **kwargs):
        if request.method == "GET":
            return super().retrieve(request, *args, **kwargs)
        elif request.method == "PUT":
            return super().update(request, *args, **kwargs)
        elif request.method == "PATCH":
            return super().partial_update(request, *args, **kwargs)
