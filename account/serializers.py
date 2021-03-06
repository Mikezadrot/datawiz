from django.contrib.auth import get_user_model
from rest_framework import serializers, exceptions
from rest_framework.serializers import ModelSerializer, Serializer
from django.contrib.auth.password_validation import validate_password

from core.serializers import BaseModelSerializer

User = get_user_model()


class UserSerializer(BaseModelSerializer):

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name')


# class GroupSerializer(BaseModelSerializer):
#     user = UserSerializer()
#
#
# class CommentSerializer(BaseModelSerializer):
#     pass
#
#
# class PostSerializer(BaseModelSerializer):
#     author_id = serializers.PrimaryKeyRelatedField()
#     comments = CommentSerializer(many=True, read_only=True)
# class UserBaseSerializer(Serializer):
#     id = serializers.IntegerField(read_only=True)
#     first_name = serializers.CharField(max_length=30, allow_blank=True, allow_null=True)
#     email = serializers.EmailField(required=True,
#                                    validators=[
#                                        validators.UniqueValidator(
#                                            queryset=User.objects.all(),
#                                        )
#
#                                    ])
#     password = serializers.CharField()
#
#     def validete_password(self, password):
#         if not validate_password(password):
#             raise exceptions.ValidationError('Password invalid')
#         return password
#
#     def validate_email(self, email):
#         if email.endswith(("datawiz.io", "@nielson.com")):
#             raise exceptions.ValidationError(detail="This email dont exist")
#
#     def validate(self, attrs):
#         attrs = super().validate(attrs)
#
#     def create(self, validated_data):
#         return User.objects.create_user()
#
#     def update(self, instance, validate_data):
#         instance.__dict__.update(**validate_data)
#         instance.save()
#     class Meta:
#         model = User
