from django.contrib.auth.models import User
from django.db import models


class AuthorizationCode(models.Model):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE)
    code = models.TextField()


class Word(models.Model):
    key_word = models.TextField()
    users = models.ManyToManyField(to=User, related_name="words")
    last_search = models.DateTimeField(null=True)


class Video(models.Model):
    words = models.ManyToManyField(to=Word, related_name="videos")
    video_id = models.TextField(unique=True)
    title = models.TextField()
    published_at = models.DateTimeField()

    @property
    def get_url(self):
        return f"https://www.youtube.com/watch?v={self.video_id}"
