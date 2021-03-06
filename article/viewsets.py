from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework_extensions.routers import ExtendedDefaultRouter
from core.viewsets import BaseModelViewSet
from .filter import PostFilter

from .models import Post, Comment, Like
from .serializers import PostSerializer, CommentSerializer


class PostViewSet(BaseModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    filter_backends = [SearchFilter, OrderingFilter, DjangoFilterBackend]
    search_filter = ['title', 'author__first_name', 'author__last_name']
    ordering = ['created']
    ordering_fields = ['title', 'author__username']
    filterset_class = PostFilter

    @action(methods=["POST"], detail=True, url_path='do_like')
    def like(self, request, *args, **kwargs):
        session = request.session.session_key
        return Response("")


class CommentViewSet(BaseModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [AllowAny]

    def get_serializer(self, *args, **kwargs):
        if kwargs.get('data'):
            kwargs['data'].updata(self.get_parsers_query_dict())
            return super(CommentViewSet, self).get_serializer(*args, **kwargs)
