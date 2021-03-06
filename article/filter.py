import django_filters
from .models import Post, Comment
from django.contrib.auth.models import User


class PostFilter(django_filters.FilterSet):
    class Meta:
        model = Post
        fields = ['author', 'title', 'created']


class CommentFilter(django_filters.FilterSet):
    class Meta:
        model = Comment
        fields = ['author', 'post']


class UserFilter(django_filters.FilterSet):
    class Meta:
        model = User
        fields = ['id', 'first_name']
