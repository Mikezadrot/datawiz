from django.contrib.auth import get_user_model
from rest_framework import viewsets
from core.serializers import BaseModelSerializer


User = get_user_model()


class UserViewSet(BaseModelSerializer):
    queryset = User.objects.all()
    serializer_class = BaseModelSerializer
