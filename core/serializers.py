from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.authtoken.models import Token

from core.models import Word, Video


class WordSerializer(serializers.ModelSerializer):

    class Meta:
        model = Word
        fields = ["key_word", "id"]


class VideoSerializer(serializers.ModelSerializer):
    url = serializers.CharField(source="get_url")

    class Meta:
        model = Video
        fields = ["id", "url", "title"]


class SighupUserSerializer(serializers.ModelSerializer):
    token = serializers.CharField(source="auth_token.key", read_only=True)

    class Meta:
        model = User
        fields = ("id", "username", "password", "token")
        extra_kwargs = {
            "password": {"write_only": True},
        }

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data.get("username"),
            password=validated_data.get("password")
        )
        Token.objects.create(user=user)
        return user
