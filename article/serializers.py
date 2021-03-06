from django.contrib.auth import get_user_model

from core.serializers import BaseModelSerializer
from rest_framework import serializers

from .models import Post, Comment, Like

User = get_user_model()


class CommentSerializer(BaseModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'author', 'body')


class PostSerializer(BaseModelSerializer):
    author_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), source="author"
    )
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ('id', 'slug', 'title', 'body', 'comments', 'author_id')

# class LikeSerializer(BaseModelSerializer):

