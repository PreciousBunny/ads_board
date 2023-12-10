from django.shortcuts import get_object_or_404
from rest_framework import pagination, viewsets
from rest_framework.decorators import action
from django_filters.rest_framework import DjangoFilterBackend
from ads.filters import AdFilter
from ads.models import Ad, Comment
from ads.serializers import AdSerializer, CommentSerializer, AdDetailSerializer
from ads.permissions import AdminOrOwner
from rest_framework.permissions import IsAuthenticated, AllowAny


class AdPagination(pagination.PageNumberPagination):
    """
    Пагинация страниц для модели Ad.
    """
    page_size = 4
    page_size_query_param = 'page_size'
    max_page_size = 50


# view функции. Предлагаем Вам следующую структуру - но Вы всегда можете использовать свою
class AdViewSet(viewsets.ModelViewSet):
    queryset = Ad.objects.select_related('author').all()
    serializer_class = AdSerializer
    pagination_class = AdPagination
    filter_backends = (DjangoFilterBackend,)
    filterset_class = AdFilter

    def get_serializer_class(self):
        if self.action in ('retrieve', 'create', 'update', 'destroy'):
            return AdDetailSerializer
        return AdSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_permissions(self):
        self.permission_classes = (AllowAny,)
        if self.action in ('create', 'retrieve', 'update', 'partial_update', 'destroy', 'me'):
            self.permission_classes = (AdminOrOwner,)
        return tuple(permission() for permission in self.permission_classes)

    @action(detail=False, methods=('get',))
    def me(self, request, *args, **kwargs):
        self.queryset = Ad.objects.filter(author=self.request.user).all()
        return super().list(self, request, *args, **kwargs)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_queryset(self):
        return Comment.objects.select_related('author').select_related('ad').filter(ad__id=self.kwargs['ad_pk'])

    def perform_create(self, serializer):
        serializer.save(
            author=self.request.user,
            ad=get_object_or_404(Ad, id=self.kwargs['ad_pk'])
        )

    def get_permissions(self):
        self.permission_classes = (IsAuthenticated,)
        if self.action in ('create', 'retrieve', 'update', 'partial_update', 'destroy', 'me'):
            self.permission_classes = (AdminOrOwner,)
        return tuple(permission() for permission in self.permission_classes)
