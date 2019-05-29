from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, viewsets
from rest_framework.permissions import AllowAny

from core.filters import VideosFilter
from core.models import Word, Video
from core.serializers import SighupUserSerializer, WordSerializer, VideoSerializer


class WordViewSet(viewsets.ModelViewSet):
    serializer_class = WordSerializer
    queryset = Word.objects.all()


class VideoView(generics.ListAPIView):
    serializer_class = VideoSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = VideosFilter

    def get_queryset(self):
        return Video.objects.filter(words__users=self.request.user).order_by("-published_at")


class SighupView(generics.CreateAPIView):
    authentication_classes = []
    permission_classes = (AllowAny,)
    serializer_class = SighupUserSerializer
