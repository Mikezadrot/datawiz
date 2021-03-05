import django_filters
from .models import Post, Comment
from django.contrib.auth.models import User


class PostFilter(django_filters.FilterSet):
    class Meta:
        model = Post
        fields = ['', 'release_date']


class CommentFilter(django_filters.FilterSet):
    class Meta:
        model = Comment
        fields = ['price', 'release_date']


class UserFilter(django_filters.FilterSet):
    class Meta:
        model = User
        fields = ['price', 'release_date']
