from django.contrib.auth import get_user_model
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from account.serializers import UserSerializer
from article.serializers import PostSerializer
from core.viewsets import BaseModelViewSet

User = get_user_model()


class UserViewSet(BaseModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    serializer_classes = {
        "posts": PostSerializer
    }

    @action(methods=["GET", "POST"], detail=True, url_path="posts")
    def posts(self, request, *args, **kwargs):
        user = self.get_object()
        post_data = user.posts.all()
        serializer = self.get_serializer(post_data, many=True)
        return Response(serializer.data)
